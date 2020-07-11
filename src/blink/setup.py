"""
Bootstrap the environment.
"""
import os

from dotenv import load_dotenv


def setup_env():
    # load the environment variables containing the secrets/config
    dotenv_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, ".env")
    print(dotenv_path)
    load_dotenv(dotenv_path)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blink.settings")
