#!/bin/bash
echo "🔧 Initialisation du Render Dashboard depuis image GHCR..."
mkdir -p logs
mkdir -p logs/reports
docker-compose pull
docker-compose up -d
echo "✅ Déploiement terminé sur http://localhost:8080"
