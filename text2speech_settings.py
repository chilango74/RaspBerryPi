import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[12].id)  # English
engine.setProperty('rate', 200)
engine.setProperty('volume',1.0)

