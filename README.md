# Env-Guardian for Python

<img width="1024" height="1024" alt="undefined - Imgur" src="https://github.com/user-attachments/assets/df8fc4e0-3379-4be6-b93a-4ccb71710203" />

[![PyPI version](https://badge.fury.io/py/env-guardian-py.svg)](https://badge.fury.io/py/env-guardian-py)

Un gestionnaire de configuration simple et robuste pour Python qui charge, valide et type les variables d'environnement à partir de fichiers `.env`. **Zéro dépendance externe.**

## Installation
```bash
pip install env-guardian-py
```
Utilisation
1. Créez un fichier .env à la racine de votre projet :
```bash
# Fichier .env
APP_NAME=Mon Application
PORT=3000
DEBUG_MODE=True
DATABASE_URL=postgres://user:pass@host:port/db
```
2. Utilisez Env-Guardian dans votre code:
```bash
# Fichier: config.py
from env_guardian import guardian

# Validez les variables critiques au démarrage de l'application.
# Le programme s'arrêtera si DATABASE_URL est manquant.
guardian.validate(['DATABASE_URL'])

# Créez vos variables de configuration
class Config:
    APP_NAME = guardian.get('APP_NAME', 'App par Défaut')
    PORT = guardian.get_int('PORT', 8080)
    DEBUG = guardian.get_bool('DEBUG_MODE', False)
    DB_URL = guardian.get('DATABASE_URL')

# Utilisez-les dans votre application
# print(Config.PORT)
```
### Licence
ISC


