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
    if went_to_sleep == True:
        went_to_sleep = False
    if awoken == False:
        awoken = True
    
    


def train():
 
    


    while awoken == False:
      try:
         query = wakecommand().lower()
         if 'shutdown' in query:
          Quit()
         elif 'hello' in query:
          greetings()
         
         
      except sr.UnknownValueError:
         print("I don't understand sir")

def load_trained_model():
    while went_to_sleep == True:
      try:
         query = wakecommand().lower()
         if 'shutdown' in query:
          Quit()
         elif 'hello' in query:
          greetings()
         
      except sr.UnknownValueError:
         print("I don't understand sir")
