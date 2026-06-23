from ollama import chat

from memory.memory_manager import load_memory
from memory.chat_history import (
    add_user_message,
    add_assistant_message,
    get_history
)
def ask_llm(prompt):

    memory = load_memory()

    add_user_message(prompt)

    messages = [
        {
            "role": "system",
            "content": f"""
            You are a voice assistant.

            User information:
            {memory}

            Give short, precise answers.
            Usually answer in 1-3 sentences.
            Avoid unnecessary explanations.
            """
        }
    ]

    messages.extend(get_history())

    response = chat(
        model="llama3.2",
        messages=messages
    )

    answer = response["message"]["content"]

    add_assistant_message(answer)

    return answer