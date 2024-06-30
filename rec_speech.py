import speech_recognition as sr
from cap_speech import capture_speech
# import pyaudio
# import wave

recognizer = sr.Recognizer()


def recognize_speech():
    # recognizing audio
    try:
        # text = recognizer.recognize_google(audio)
        text = recognizer.recognize_google_cloud(capture_speech())
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error fetching results; {e}")
        return ""
