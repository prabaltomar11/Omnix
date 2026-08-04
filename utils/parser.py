from config import APP_REGISTRY, WEBSITE_REGISTRY


COMMAND_WORDS = {"open": "open",
                "launch": "open",
                 "start": "open",
                 "run": "open",
                 "execute": "open",

                 "close": "close",
                 "off": "close",
                 "exit": "close",}

SPECIAL_COMMANDS = {"history": "history",
                    "exit": "exit",
                    "quit": "exit",
                    "bye": "exit",}


def extract_command(user_input):
    user_input = user_input.lower().strip()

    words = user_input.split()

    if words[0] in SPECIAL_COMMANDS:
        action = SPECIAL_COMMANDS[words[0]]

        return action, None, None

    elif words[0] in COMMAND_WORDS:
        action = COMMAND_WORDS[words[0]]   

        app_name = None
        website_name = None

        for word in words[1:]:
            if word in APP_REGISTRY:
                app_name = word
            elif word in WEBSITE_REGISTRY:
                website_name = word  
    
        return action, app_name, website_name     

    return None, None, None


