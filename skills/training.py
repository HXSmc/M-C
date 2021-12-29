from neuralintents import GenericAssistant
import sys
from MC import wakecommand, speak
import datetime

def greetings():
    speak("welcome back")
    skip = wakecommand().lower()
    if 'skip' in skip:
        return
    hour = datetime.datetime.now().hour
    if hour >= 24 and hour < 11:
        speak("good morning sir!. this is your A.I. assistant . please tell me how can I help you?")
    elif hour >= 11 and hour < 16:
        speak("good afternoon sir!. this is your A.I. assistant . please tell me how can I help you?")
    else:
        speak("good evening sir!. this is your A.I. assistant . please tell me how can I help you?")