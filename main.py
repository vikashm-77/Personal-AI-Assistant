from voice.speech import recognize
from core.assistant_core import handle_input

while True:

    user_text = recognize()

    if not handle_input(user_text):
        break