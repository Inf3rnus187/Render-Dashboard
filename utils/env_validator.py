
import os
import sys

REQUIRED_VARS = [
    "DASH_USER",
    "DASH_PASS",
    "FLASK_SECRET_KEY",
    "DEADLINE_REPO",
    "OPENSTACK_USER",
    "OPENSTACK_PASS",
    "OS_AUTH_URL",
    "OPENSTACK_PROJECT"
]

def validate_env():
    missing = [var for var in REQUIRED_VARS if not os.getenv(var)]
    if missing:
        print(f"❌ Erreur : variables d'environnement manquantes : {', '.join(missing)}")
        sys.exit(1)
    print("✅ Toutes les variables d'environnement nécessaires sont présentes.")

if __name__ == "__main__":
    validate_env()
