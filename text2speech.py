import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i, v in enumerate(voices):
    if v.id.lower() == 'english':
        print(i)
        print(v.id)
        print(v.gender)
        print(v.languages)
        print(v.name)
        print("---------------------")
# engine.setProperty('voice', voices[61].id)  # Russian
engine.setProperty('voice', voices[12].id)  # English

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

# Russian
# engine.say("Привет всем!")
# engine.say('Я говорю на скорости ' + str(rate))
# engine.runAndWait()

print(engine.isBusy())

# English
engine.say("Hello everybody!")
print(engine.isBusy())
engine.say('I"m speaking with speed ' + str(rate))
engine.runAndWait()
print(engine.isBusy())
