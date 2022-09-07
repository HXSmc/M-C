import skills.collection.MC as Skills
import skills.training as training
from neuralintents import GenericAssistant
import speech_recognition as sr
import subprocess


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
  assistant = GenericAssistant('Desktop\py-code\M-C\mainfolder\skills\intents.json',intent_methods=mappings, model_name="awoken_jarvis")
  assistant.train_model()   
  assistant.save_model(model_name="awoken_jarvis")

  opencommands = ['open', 'launch', 'run']

  while training.awoken == True:
      try:
        query = Skills.wakecommand().lower()
        '''
        for i in range(0, 2):
          if opencommands[i] in query:
            query = query.replace(opencommands[i], "")
            subprocess.Popen("C:\\Users\\GAMER\\Desktop\\{}".format(query))
        '''    
        if 'shutdown' in query:
          Skills.Quit()
          #query = query.replace(opencommands[i], "")
          #subprocess.Popen("C:\\Users\\GAMER\\Desktop\\{}".format(query))
        else:
          assistant.request(query)
         
      except sr.UnknownValueError:
        print("I don't understand sir")
    
def go_to_sleep():
  Skills.speak("going to rest mode")
  training.went_to_sleep = True
  training.load_trained_model()

jarvis()