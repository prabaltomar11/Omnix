from core.router import route
from voice.listener import listen
from utils import logger
from utils.parser import extract_command
from utils.history import add_history


def main():
    logger.info("Welcome to Omnix")

    while user_input := listen():
        if user_input.lower().strip() in ["exit", "quit", "bye"]:
            logger.info("Exiting Omnix. Goodbye!")
            break

        add_history(user_input)

        action, app_name, website_name = extract_command(user_input)

        route(action, app_name, website_name)


if __name__ == "__main__":
    main()