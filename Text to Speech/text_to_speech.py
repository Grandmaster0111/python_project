import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('volume',0.8)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
text = 'Hello sir, This is your text to speech python program working properly.'
with open('hello.txt','r') as f:
    engine.say(f.read())
    engine.runAndWait()