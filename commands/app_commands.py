import subprocess
import webbrowser 
from config import APP_REGISTRY, WEBSITE_REGISTRY
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


def open_website(website_name):
    website_name = website_name.lower().strip()

    if website_name not in WEBSITE_REGISTRY:
        logger.error(f"'{website_name}' is not a supported website.")
        return

    try:
        webbrowser.open(WEBSITE_REGISTRY[website_name])
        logger.success(f"Opening {website_name}....")
    except Exception as e:
        logger.error(f"Failed to open {website_name}: {e}")      

def close_website(website_name):
    website_name = website_name.lower().strip()

    if website_name not in WEBSITE_REGISTRY:
        logger.error(f"'{website_name}' is not a supported website.")
        return

    try:
        subprocess.run(["pkill", "-f", WEBSITE_REGISTRY[website_name]])
        logger.success(f"{website_name} closed successfully.")
    except Exception as e:
        logger.error(f"Failed to close {website_name}: {e}")             