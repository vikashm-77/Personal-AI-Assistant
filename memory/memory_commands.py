from memory.memory_manager import load_memory, save_memory
from voice.tts import speak


def handle_memory(user_text):

    # remember my X is Y
    if user_text.startswith("remember my ") and " is " in user_text:

        text = user_text.replace("remember my ", "", 1)

        key, value = text.split(" is ", 1)

        key = (
                key.strip()
                .lower()
                .replace(" ", "_")
                .rstrip(".,!?")
            )
        value = value.strip().rstrip(".,!?").title()

        memory = load_memory()

        memory[key] = value

        save_memory(memory)

        speak(f"I will remember your {key.replace('_', ' ')}")

        return True

    # what is my X
    if user_text.startswith("what is my "):

        key = user_text.replace("what is my ", "", 1)

        key = (
                key.strip()
                .lower()
                .replace(" ", "_")
                .rstrip(".,!?")
            )

        memory = load_memory()

        if key in memory:

            speak(
                f"Your {key.replace('_', ' ')} is {memory[key]}"
            )

        else:
            speak(
                f"I don't know your {key.replace('_', ' ')} yet"
            )

        return True
    if "what do you know about me" in user_text:

        memory = load_memory()

        if not memory:
            speak("I don't know anything about you yet.")
            return True

        response = "I know "

        for key, value in memory.items():
            response += f"your {key.replace('_', ' ')} is {value}. "

        speak(response)

        return True
    
    if user_text.startswith("forget my "):

        key = user_text.replace("forget my ", "", 1)

        key = (
                key.strip()
                .lower()
                .replace(" ", "_")
                .rstrip(".,!?")
            )

        memory = load_memory()

        if key in memory:

            del memory[key]

            save_memory(memory)

            speak(f"I forgot your {key.replace('_', ' ')}")

        else:

            speak("I don't know that information")

        return True

    return False