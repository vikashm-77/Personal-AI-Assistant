import webbrowser
from voice.tts import speak

sites = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "spotify": "https://open.spotify.com",
    "chatgpt": "https://chatgpt.com",
    "github": "https://github.com"
}

def open_site(user_text):

    if not user_text.startswith("open"):
        return False

    website = user_text.replace("open", "").strip()

    if website in sites:
        speak(f"Opening {website}")
        webbrowser.open(sites[website])
        return True

    return False

