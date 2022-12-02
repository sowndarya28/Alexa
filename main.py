import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
quite = False
mode = "text"


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        if(mode=="talk"):
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                commands = listener.recognize_google(voice)
                commands = commands.lower()
                if 'alexa' in commands:
                    commands = commands.replace('alexa', '')
                    print(commands)
        else:
            print("Please type your command")
            commands=input()
            if 'alexa' in commands:
                commands = commands.replace('alexa', '')
                print(commands)
    except:
        pass
    return commands


def run_alexa():
    quite =  False
    commands = take_command()
    print(commands)
    if 'play' in commands:
        song = commands.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in commands:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'what is the meaning of' in commands:
        person = commands.replace('what is the meaning of', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'quit the program' in commands:
        print('quitting')
        quite = True

    else:
        talk('Please say the command again.')






while True:
    if quite:
        break

    run_alexa()
