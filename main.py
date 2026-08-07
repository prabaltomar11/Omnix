from core.router import route
from voice.listener import listen
from utils import logger
from utils.parser import extract_command
import utils.history
from voice.listener import listen


def choose_input_mode():
        while True:

            mode = input("Choose input mode:\n 1. Text\n 2. Voice\n").strip().lower()
            if mode in ["1", "text"]:
                return "text"
            
            elif mode in ["2", "voice"]:
                return "voice"
            
            else:
                logger.error("Invalid input mode. Please choose 'text' or 'voice'.")

def main():
    logger.info(" Hello Sir.\nWelcome to Omnix")
    mode = choose_input_mode()

    while True:
         user_input = listen(mode)

         if user_input is None:
            logger.error("No input received. Please try again.")
            continue

         if user_input.lower().strip() in ["exit", "quit", "bye"]:
            logger.success("Exiting Omnix. Goodbye Sir!")
            break

       
         utils.history.add_history(user_input)

         action, app_name, website_name = extract_command(user_input)

         route(action, app_name, website_name)


if __name__ == "__main__":
    main()