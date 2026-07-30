COMMAND_WORDS = {"open": "open",
                "launch": "open",
                 "start": "open",
                 "run": "open",
                 "execute": "open",

                 "close": "close",
                 "off": "close",
                 "exit": "close",}


def extract_command(user_input):
    user_input = user_input.lower().strip()

    words = user_input.split()

    if len(words) >= 2 and words[0] in COMMAND_WORDS:

        action = COMMAND_WORDS[words[0]]
        app_name = " ".join(words[1:])

        return action, app_name
    


   


