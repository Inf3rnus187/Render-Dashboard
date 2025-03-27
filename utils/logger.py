
import datetime

def log_event(message):
    with open("logs/audit.log", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")

def get_audit_logs():
    with open("logs/audit.log", "r") as f:
        return f.readlines()
