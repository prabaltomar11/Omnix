def dispatch(user_input):
    command = user_input.lower().strip()

    if command.startswith(("profile", "change profile", "update profile")):
        return "profile"

    if command.startswith(("open", "close", "history", "exit", "quit", "bye", "stop")):
        return "router"

    return "ai"
     