import webbrowser


sites = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "spotify": "https://open.spotify.com",
    "chatgpt": "https://chatgpt.com",
    "github": "https://github.com"
}

def open_site(user_text):

    if not user_text.startswith("open"):
        return None

    website = user_text.replace("open", "").strip()

    if website in sites:
        webbrowser.open(sites[website])
        return f"Opening {website}"

    return None

