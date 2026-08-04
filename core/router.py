from config import WEBSITE_REGISTRY
from config import APP_REGISTRY
from commands.app_commands import close_app, open_app, open_website, close_website
from utils import logger
from utils.history import show_history


def route(action, app_name, website_name): 


    if action == "history":
        history = show_history()
        if history:
            logger.info("Command History:")
            for i, command in enumerate(history, start=1):
                logger.info(f"{i}. {command}")
        else:
            logger.info("No command history available.")
     
    elif action == "open":
        if app_name in APP_REGISTRY:
            open_app(app_name)
        elif website_name in WEBSITE_REGISTRY:
            open_website(website_name)
        else:
            logger.error("That is not supported.")

    elif action == "close":
        if app_name in APP_REGISTRY:
            close_app(app_name)
        elif website_name in WEBSITE_REGISTRY:
            close_website(website_name)
        else:
            logger.error("That is not supported.")


       