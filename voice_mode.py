voice_enabled = False

def enable_voice():
    global voice_enabled
    voice_enabled = True

def disable_voice():
    global voice_enabled
    voice_enabled = False

def is_voice_enabled():
    return voice_enabled
