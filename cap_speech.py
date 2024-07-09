import speech_recognition as sr


def capture_speech():
    # capturing audio
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognition successful.")
            return audio
        except sr.WaitTimeoutError:
            print("Timeout. No speech detected.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")

    return None
