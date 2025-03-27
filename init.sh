#!/bin/bash
echo "Initialisation de l’environnement…"
cp .env.example .env
mkdir -p logs
mkdir -p logs/reports
docker-compose build
docker-compose up -d
