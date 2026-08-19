def dispatch(user_input):
    command = user_input.lower().strip()

    if command.startswith(( "time",
    "date",
    "today",
    "current time",
    "current date",
    "aaj",
    "aajki date",
    "aaj ki date",
    "aaj ka time",
    "abhi ka time")):

        return "time"

    if command.startswith(("profile", "change profile", "update profile")):
        return "profile"

    if command.startswith(("open", "close", "history", "exit", "quit", "bye", "stop")):
        return "router"

    if command.startswith(("voice on", "voice off")):
        return "voice"

    return "ai"
