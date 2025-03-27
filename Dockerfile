
FROM python:3.11-slim

WORKDIR /app
COPY . /app

# Installation des dépendances système nécessaires pour openstacksdk
RUN apt-get update && \
    apt-get install -y gcc libffi-dev libssl-dev python3-dev libpq-dev curl && \
    apt-get clean

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir openstacksdk

# Création du dossier de logs
RUN mkdir -p /app/logs

EXPOSE 8080

CMD ["python", "dashboard.py"]
