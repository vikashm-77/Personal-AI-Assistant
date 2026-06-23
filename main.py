from voice.speech import recognize
from command_handler import process_command


while True:

    user_text = recognize()

    if not process_command(user_text):
        break