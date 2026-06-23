import os
import speech_recognition as sr
import whisper
from voice.tts import speak

r = sr.Recognizer()

print("Loading Whisper...")
model = whisper.load_model("small")
print("Whisper Ready!")

def recognize():
    try:
        with sr.Microphone() as source:

            r.adjust_for_ambient_noise(source, duration=1)

            print("Speak something...")

            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        temp_file = "temp.wav"

        with open(temp_file, "wb") as f:
            f.write(audio.get_wav_data())

        result = model.transcribe(
            temp_file,
            language="en",
            fp16 = False
        )

        text = result["text"].lower().strip()

        if os.path.exists(temp_file):
            os.remove(temp_file)

        print("You said:", text)

        return text

    except sr.WaitTimeoutError:

        print("No speech detected")

        speak("No speech detected please try again")

    except Exception as e:

        print("Error:", e)

    return None