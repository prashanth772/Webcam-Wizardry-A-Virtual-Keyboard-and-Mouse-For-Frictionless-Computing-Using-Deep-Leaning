import pyttsx3

def speak(Text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)

    # Speak the given text
    print(f"Speaking: {Text}")
    engine.say(text=Text)
    engine.runAndWait()

# speak("He. speaks. something")