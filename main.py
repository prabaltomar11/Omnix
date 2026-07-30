from commands.app_commands import close_app, open_app
from utils import logger
from utils.parser import extract_command


def main():
    logger.info("Welcome to Omnix")



    user_input = input("What can I do for you? ")

    action, app_name = extract_command(user_input)

    if action is None:
        logger.error("Invalid command.")
        return



    if action == "open":
        open_app(app_name)
    elif action == "close":
        close_app(app_name)



if __name__ == "__main__":
    main()