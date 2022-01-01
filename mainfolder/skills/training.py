from neuralintents import GenericAssistant
import sys
import speech_recognition as sr
from skills.collection.MC import wakecommand, speak, Quit
import datetime


awoken = False

def greetings():
    global awoken
    speak("welcome back")
    skip = wakecommand().lower()
    if 'skip' in skip:
        if awoken == False:
         awoken = True
        return   
    hour = datetime.datetime.now().hour
    if hour >= 24 and hour < 11:
        speak("good morning sir!. this is your A.I. assistant . please tell me how can I help you?")
    elif hour >= 11 and hour < 16:
        speak("good afternoon sir!. this is your A.I. assistant . please tell me how can I help you?")
    else:
        speak("good evening sir!. this is your A.I. assistant . please tell me how can I help you?")
    if awoken == False:
       awoken = True
    
    
        
        


def train():
    

    mappings = {
      "greeting": greetings,
      "shutdown": Quit
    }
    assistant = GenericAssistant('mainfolder\skills\intents.json',intent_methods=mappings, model_name="resting")
    assistant.train_model()
    assistant.save_model(model_name="resting")
    #assistant.load_model(model_name="resting")

 
    


    while awoken == False:
      try:
         query = wakecommand().lower()
         assistant.request(query)
         
      except sr.UnknownValueError:
         print("I don't understand sir")

