GREETINGS = {
    "hello",
    "hi",
    "hey",
    "good morning",
    "good afternoon",
    "good evening"
}

def greet(user_text):

    for greeting in GREETINGS:

        if user_text.startswith(greeting):

            return "Hello! How can I help you?"

    return None