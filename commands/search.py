import webbrowser
from urllib.parse import quote_plus




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
                return "What should I search?"

            webbrowser.open(
                f"https://www.google.com/search?q={quote_plus(query)}"
            )

            return f"Searching Google for {query}"

    return None

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
                return "What should I search on YouTube?"

            webbrowser.open(
                f"https://www.youtube.com/results?search_query={quote_plus(query)}"
            )

            return f"Searching YouTube for {query}"

    return None
