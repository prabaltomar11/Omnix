import subprocess
from config import APP_REGISTRY
from utils import logger


def open_app(app_name):
    app_name = app_name.lower().strip()

    if app_name not in APP_REGISTRY:
        logger.error(f"'{app_name}' is not a supported application.")
        return

    try:
        subprocess.Popen([APP_REGISTRY[app_name]])
        logger.success(f"{app_name} opened successfully.")
    except FileNotFoundError:
        logger.error(f"{app_name} is installed but launch command was not found.")


def close_app(app_name):
    app_name = app_name.lower().strip()

    if app_name not in APP_REGISTRY:
        logger.error(f"'{app_name}' is not a supported application.")
        return

    try:
        subprocess.run(["pkill", "-f", APP_REGISTRY[app_name]])
        logger.success(f"{app_name} closed successfully.")
    except Exception as e:
        logger.error(f"Failed to close {app_name}: {e}")        