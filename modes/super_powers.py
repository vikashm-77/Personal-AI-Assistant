from voice.tts import speak
from vision.gesture_mode import gesture_mode

SUPER_POWER_COMMANDS = [
    "switch to super powers",
    "switch to super power",
    "super powers mode",
    "super power mode",
    "activate super powers",
    "activate super power",
    "open super powers",
    "open super power mode"
]

def is_super_power_command(user_text):
    return any(cmd in user_text for cmd in SUPER_POWER_COMMANDS)

def start_super_powers():

    speak("Super powers activated")

    gesture_mode()

    speak("Returning to voice mode")

    return True