from voice.tts import speak

CHAT_MODE = False

def handle_chat_mode(user_text):

    global CHAT_MODE

    if "enter chat mode" in user_text:
        CHAT_MODE = True
        speak("Chat mode activated")
        return True

    if "exit chat mode" in user_text:
        CHAT_MODE = False
        speak("Chat mode deactivated")
        return True

    return False


def is_chat_mode():
    return CHAT_MODE