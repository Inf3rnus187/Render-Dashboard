# Render Dashboard 🚀

Dashboard Web pour le suivi et l'autoscaling de rendu cloud avec Deadline + OpenStack.

## 📦 Installation rapide

```bash
git clone https://monrepo/render-dashboard.git
cd render-dashboard
chmod +x init.sh
./init.sh
```

Ou avec `make` :

```bash
make init
```

## 🔐 Accès
- URL : http://localhost:8080
- Login : `admin / monpass`

## 🧩 Fonctionnalités
- Autoscaling Deadline + OpenStack
- Auth multi-utilisateur (admin/viewer)
- Interface Web (Flask + Chart.js)
- Alertes Slack / Email
- Rapports PDF + Historique
- Création d’utilisateurs via interface
- Page d’audit avec export CSV

## 🕒 Cron Autoscaler
```bash
*/10 * * * * docker exec deadline_dashboard python utils/autoscaler.py
```

## 📁 Structure des logs

- `logs/actions.log` : historique des scalings, actions utilisateur
- `logs/errors.log` : erreurs système ou réseau
- `logs/jobs.csv` : export des jobs pour reporting
- `logs/reports/` : PDF de rapports générés

## 🔒 Authentification LDAP (optionnelle)

Configurer dans `.env` :

```env
LDAP_ENABLED=true
LDAP_HOST=ldap://your.ldap.server
LDAP_BASE_DN=dc=domain,dc=com
LDAP_BIND_USER=cn=readonly,dc=domain,dc=com
LDAP_BIND_PASS=motdepasse
```

Le dashboard passera automatiquement en mode LDAP via Flask-LDAP3-Login.

## 📦 Déploiement en production

Pour production, utiliser :

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

Fichier `docker-compose.prod.yml` à créer avec :

```yaml
services:
  dashboard:
    environment:
      - FLASK_ENV=production
    restart: always
```
