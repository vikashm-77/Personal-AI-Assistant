from voice.tts import speak

CHAT_MODE = False

def handle_chat_mode(user_text):

    global CHAT_MODE

    if "enter chat mode" in user_text:
        CHAT_MODE = True
        return "Chat mode activated"

    if "exit chat mode" in user_text:
        CHAT_MODE = False
        return "Chat mode deactivated"

    return None


def is_chat_mode():
    return CHAT_MODE