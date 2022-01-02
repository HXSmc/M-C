from neuralintents import GenericAssistant
import sys
import speech_recognition as sr
from skills.collection.MC import wakecommand, speak, Quit
import datetime


awoken = False

went_to_sleep = False

def greetings():
    global awoken
    global went_to_sleep
    speak("welcome back")
    skip = wakecommand().lower()
    if 'skip' in skip:
        if went_to_sleep == True:
         went_to_sleep = False
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
    if went_to_sleep == True:
       went_to_sleep = False
    
mappings = {
      "greeting": greetings
    }    
assistant = GenericAssistant('mainfolder\skills\intents.json',intent_methods=mappings, model_name="resting")


def train():
    

    
    global assistant
    assistant.train_model()
    assistant.save_model(model_name="resting")

 
    


    while awoken == False:
      try:
         query = wakecommand().lower()
         if 'shutdown' in query:
          Quit()
         else:
          assistant.request(query)
         
         
      except sr.UnknownValueError:
         print("I don't understand sir")

def load_trained_model():
    print("Loading trained model")
    global assistant
    assistant.load_model(model_name="resting")

    while went_to_sleep == True:
      try:
         query = wakecommand().lower()
         if 'shutdown' in query:
          Quit()
         else:
          assistant.request(query)
         
      except sr.UnknownValueError:
         print("I don't understand sir")
