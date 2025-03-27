
from utils.env_validator import validate_env
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from config import Config, User
from utils.deadline_api import get_jobs, get_job_summary
from utils.openstack_api import get_workers, scale_up, scale_down
from utils.logger import log_event, get_audit_logs
import json

validate_env()

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    return User(username)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == Config.USERNAME and request.form['password'] == Config.PASSWORD:
            login_user(User(Config.USERNAME))
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    job_summary = get_job_summary()
    jobs = get_jobs()
    workers = get_workers()
    return render_template("dashboard.html", jobs=jobs, workers=workers, job_summary=job_summary)

@app.route('/scale-up', methods=['POST'])
@login_required
def scale_up_route():
    if current_user.role != "admin":
        return "Accès interdit", 403
    scale_up()
    log_event(f"SCALE-UP déclenché par {current_user.id}")
    return redirect(url_for('dashboard'))

@app.route('/scale-down', methods=['POST'])
@login_required
def scale_down_route():
    if current_user.role != "admin":
        return "Accès interdit", 403
    scale_down()
    log_event(f"SCALE-DOWN déclenché par {current_user.id}")
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/admin/audit')
@login_required
def audit():
    if current_user.role != "admin":
        return "Accès interdit", 403
    logs = get_audit_logs()
    return render_template("audit.html", logs=logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

@app.route('/admin/config')
@login_required
def config_status():
    if current_user.role != "admin":
        return "Accès interdit", 403
    config_vars = {key: os.getenv(key, '[NON DÉFINI]') for key in sorted(os.environ.keys()) if key.startswith(('DASH_', 'FLASK_', 'DEADLINE_', 'OPENSTACK_', 'OS_', 'LDAP_', 'EMAIL_'))}
    return render_template("config.html", config_vars=config_vars)

@app.route('/job/<job_id>/suspend', methods=['POST'])
@login_required
def suspend(job_id):
    from utils.deadline_api import suspend_job
    if current_user.role != 'admin':
        return "Non autorisé", 403
    suspend_job(job_id)
    return redirect(url_for('dashboard'))

@app.route('/job/<job_id>/resume', methods=['POST'])
@login_required
def resume(job_id):
    from utils.deadline_api import resume_job
    if current_user.role != 'admin':
        return "Non autorisé", 403
    resume_job(job_id)
    return redirect(url_for('dashboard'))
