import speech_recognition as sr


recognizer = sr.Recognizer()


def capture_speech():
    # capturing audio
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        return audio
