import os
from pathlib import Path

class EnvGuardian:
    def __init__(self, env_path=None):
        """Charge les variables depuis le .env et l'environnement système."""
        self._config = {}
        
        # Charge d'abord depuis l'environnement système
        for key, value in os.environ.items():
            self._config[key] = value

        # Trouve et charge le fichier .env
        try:
            # Le chemin est relatif à l'endroit où le script est lancé
            dotenv_path = Path(env_path or Path.cwd() / '.env')
            if dotenv_path.is_file():
                with dotenv_path.open() as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            key, value = line.split('=', 1)
                            # Ne remplace pas une variable déjà définie par le système
                            if key not in self._config:
                                self._config[key] = value.strip()
        except Exception:
            # Ignore si le fichier .env n'est pas trouvé ou est invalide
            pass

    def get(self, key, default=None):
        """Récupère une variable en tant que chaîne de caractères."""
        return self._config.get(key, default)

    def validate(self, required_keys):
        """Vérifie que les variables requises sont présentes."""
        missing_keys = [key for key in required_keys if key not in self._config]
        if missing_keys:
            raise ValueError(f"Erreur de Configuration: Variables d'environnement manquantes: {', '.join(missing_keys)}")

    def get_int(self, key, default=None):
        """Récupère une variable en tant qu'entier."""
        value = self.get(key)
        if value is None:
            return default
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    def get_bool(self, key, default=False):
        """Récupère une variable en tant que booléen."""
        value = self.get(key, str(default))
        return value.lower() in ('true', '1', 't', 'y', 'yes')

# On exporte une seule instance, prête à l'emploi (Singleton Pattern)
guardian = EnvGuardian()
