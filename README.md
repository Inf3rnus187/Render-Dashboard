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
