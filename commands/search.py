import webbrowser
from urllib.parse import quote_plus

from voice.tts import speak



def google_search(user_text):

    prefixes = [
        "search google for",
        "google",
        "search",
        "look up",
        "find"
    ]

    for prefix in prefixes:

        if user_text.startswith(prefix):

            query = user_text[len(prefix):].strip()

            if not query:
                speak("What should I search?")
                return True

            speak(f"Searching Google for {query}")

            webbrowser.open(
                f"https://www.google.com/search?q={quote_plus(query)}"
            )

            return True

    return False

def youtube_search(user_text):

    prefixes = [
        "search youtube for",
        "youtube",
        "play on youtube"
    ]

    for prefix in prefixes:

        if user_text.startswith(prefix):

            query = user_text[len(prefix):].strip()

            if not query:
                speak("What should I search on YouTube?")
                return True

            speak(f"Searching YouTube for {query}")

            webbrowser.open(
                f"https://www.youtube.com/results?search_query={quote_plus(query)}"
            )

            return True

    return False
