import pyttsx3

def text_to_speech(text):    
    engine = pyttsx3.init()

    # for female voice set 1
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # for speed of message
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 'rate=150')

    engine.say(text)
    engine.runAndWait()
    
# text_to_speech("hello, I am your Voice Taskmate. How can I help you?")    