import subprocess

apps = {
    "chrome": "Google Chrome",
    "vscode": "Visual Studio Code",
    "spotify": "Spotify",
    "calculator": "Calculator"
}

def open_app(user_text):

    if not user_text.startswith("open"):
        return None

    for key, app_name in apps.items():

        if key in user_text:

            try:
                subprocess.run(["open", "-a", app_name])

                return f"Opening {key}"

            except Exception:
                return "Unable to open application"

    return None