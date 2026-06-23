import subprocess
from voice.tts import speak

apps = {
    "chrome": "Google Chrome",
    "vscode": "Visual Studio Code",
    "spotify": "Spotify",
    "calculator": "Calculator"
}

def open_app(user_text):

    if not user_text.startswith("open"):
        return False

    for key, app_name in apps.items():

        if key in user_text:

            try:
                subprocess.run(["open", "-a", app_name])

                speak(f"Opening {key}")

                return True

            except Exception:
                speak("Unable to open application")
                return True

    return False