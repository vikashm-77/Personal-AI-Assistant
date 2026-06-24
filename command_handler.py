from voice.tts import speak
from llm import ask_llm
from memory.memory_commands import handle_memory

from commands.time_handler import handle_time_date
from commands.search import google_search, youtube_search
from commands.apps import open_app
from commands.websites import open_site
from commands.greetings import greet

from modes.super_powers import (
    start_super_powers,
    is_super_power_command
)
from modes.chat_mode import handle_chat_mode, is_chat_mode

EXIT_COMMANDS = {
    "exit",
    "quit",
    "close assistant",
    "shutdown assistant"
}

def process_command(user_text):

    if not user_text:
        return ""

    user_text = user_text.lower().strip()

    response = handle_memory(user_text)
    if response:
        speak(response)
        return response

    # Exit
    for cmd in EXIT_COMMANDS:
        if cmd in user_text:
            speak("Goodbye")
            return "GoodBye"
   
    # Greetings
    response = greet(user_text)
    if response:
        speak(response)
        return response

    # Chat mode toggle
    response = handle_chat_mode(user_text)
    if response:
        speak(response)
        return response

    # Chat mode active
    if is_chat_mode():
        try:
            response = ask_llm(user_text)
            speak(response)
            return response
        except Exception as e:
            print(e)
            speak("Sorry, I couldn't contact Ollama.")
            return "Sorry, I couldn't contact Ollama."

    # Super Powers Mode
    if is_super_power_command(user_text):
        return start_super_powers()
    
    # Searches
    response = youtube_search(user_text)
    if response:
        speak(response)
        return response

    response = google_search(user_text)
    if response:
        speak(response)
        return response

    # Time
    response = handle_time_date(user_text)
    if response:
        speak(response)
        return response

    # Apps
    response = open_app(user_text)
    if response:
        speak(response)
        return response

    # Websites
    response = open_site(user_text)
    if response:
        speak(response)
        return response

    # Default → Ollama
    try:
        response = ask_llm(user_text)
        speak(response)
        return response

    except Exception as e:
        print(e)
        speak("Sorry, I couldn't contact Ollama.")
        return "Sorry, I couldn't contact Ollama."