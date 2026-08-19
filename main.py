from core.router import route
from voice.listener import listen
from utils import logger
from utils.parser import extract_command
import utils.history
from voice.listener import listen
from core.dispatcher import dispatch
from ai.client import ask_ai
from ai.user_profile import profile_exists, set_profile, save_profile, load_profile, update_profile
from core.tools.time_tool import get_current_datetime
from voice_mode import enable_voice, disable_voice, is_voice_enabled
from tts.speaker import speak

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

    if profile_exists():
        load_profile()

    else:
        set_profile()
        save_profile()


    logger.info(" Hello Sir.\nWelcome to Omnix")
    mode = choose_input_mode()

    while True:
         user_input = listen(mode)

         if user_input is None:
            logger.error("No input received. Please try again.")
            continue

         if user_input.lower().strip() in ["exit", "quit", "bye", "stop"]:
            logger.success("Exiting Omnix. Goodbye Sir!")
            break

         destination = dispatch(user_input)
         logger.info(f"Command routing to: {destination}")
         
         if destination == "ai":
             answer = ask_ai(user_input)
             print(answer)

             if is_voice_enabled():
                 speak(answer)

         elif destination == "time":
             now =  get_current_datetime()
             print(now)

         elif destination == "profile":
             update_profile()

         elif destination == "voice":

           command = user_input.lower().strip()

           if command == "voice on":
                enable_voice()
                print("Voice mode: ON")

           elif command == "voice off":
                disable_voice()
                print("Voice mode: OFF")

         utils.history.add_history(user_input)

         action, app_name, website_name = extract_command(user_input)

         route(action, app_name, website_name)


if __name__ == "__main__":
    main()