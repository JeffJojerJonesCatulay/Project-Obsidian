import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
for voice in voices:
    engine.setProperty('voice', voice.id)
engine.runAndWait()


def speak(text):
    engine.say(text)
    engine.runAndWait()
