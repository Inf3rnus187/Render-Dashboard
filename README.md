# Dashboard Rendu Cloud

## Installation rapide
```bash
git clone https://monrepo/render-dashboard.git
cd render-dashboard
chmod +x init.sh
./init.sh
```

## Accès
- URL : http://localhost:8080
- Login : `admin / monpass`

## Fonctionnalités
- Autoscaling Deadline + OpenStack
- Auth multi-utilisateur (admin/viewer)
- Interface web Flask + Chart.js
- Alertes Slack / Email
- Rapports PDF + Audit

## Cron recommandé
```bash
*/10 * * * * docker exec deadline_dashboard python utils/autoscaler.py
```
