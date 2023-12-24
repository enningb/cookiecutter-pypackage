"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'


import logging
from pathlib import Path

logger = logging.getLogger(__name__)

APP_NAME = '{{ cookiecutter.pkg_name }}'
DOT_APP_NAME = '.' + APP_NAME
APP_DIR = Path.home() / DOT_APP_NAME
# create config directory if it does not exist.

Path(APP_DIR).mkdir(parents=True, exist_ok=True)

CONFIG_FILE = APP_DIR / "config.INI"

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"

logging.basicConfig(format=FORMAT, level=logging.INFO)
