from orator import DatabaseManager, Model
from yaml import safe_load as yaml_load
from pathlib import Path

__all__ = ['db', 'DATABASES']

cfg_path = Path('') / 'orator.yaml'
with open(cfg_path, 'r') as file:
    cfg = yaml_load(file)
    file.close()

DATABASES = cfg.get('databases')

db = DatabaseManager(DATABASES)
Model.set_connection_resolver(db)
