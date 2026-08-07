from utils import logger
import speech_recognition as sr

def listen(mode):

    if mode == "text":
        return listen_from_text()
    
    elif mode == "voice":
        return listen_from_voice()
    
    else:
        raise ValueError("Invalid mode. Please choose 'text' or 'voice'.")

def listen_from_text():
        user_input = input("Enter your command: ")
        return user_input

def listen_from_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source)
        logger.info("Listening for your command...")

        try:
            audio = recognizer.listen(
                source,
                timeout=8,
                phrase_time_limit=10
            )

            user_input = recognizer.recognize_google(audio)
            logger.info(f"You said: {user_input}")
            return user_input
        
        except sr.WaitTimeoutError:
            logger.error("Listening timed out while waiting for phrase to start.")
            return None
        
        except sr.UnknownValueError:
            logger.error("Could not understand the audio.")
            return None
        
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google Speech Recognition service; {e}")
            return None


        