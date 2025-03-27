#!/bin/bash
echo "🔧 Initialisation du Render Dashboard..."
mkdir -p logs
mkdir -p logs/reports
docker-compose build
docker-compose up -d
echo "✅ Déploiement terminé sur http://localhost:8080"
