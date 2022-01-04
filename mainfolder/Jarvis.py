import skills.collection.MC as Skills
import skills.training as training
from neuralintents import GenericAssistant
import speech_recognition as sr


training.train()


def jarvis():
  print("back online")
  mappings = {
      "joke": Skills.joke,
      "rest": go_to_sleep,
      "play music": Skills.playmusic,
      "Cpu": Skills.cpu,
      "wikipedia": Skills.wikipedia,
      "chorme search": Skills.chorme,
      "netflix": Skills.netflix,
      "spill": Skills.spiller,
      "game idea's": Skills.game_idea
    }
  assistant = GenericAssistant('mainfolder\skills\intents.json',intent_methods=mappings, model_name="awoken_jarvis")
  assistant.train_model()   
  assistant.save_model(model_name="awoken_jarvis")



  while training.awoken == True:
      try:
        query = Skills.wakecommand().lower()
        if 'shutdown' in query:
          Skills.Quit()
        else:
          assistant.request(query)
         
      except sr.UnknownValueError:
        print("I don't understand sir")
    
def go_to_sleep():
  Skills.speak("going to rest mode")
  training.went_to_sleep = True
  training.load_trained_model()

jarvis()