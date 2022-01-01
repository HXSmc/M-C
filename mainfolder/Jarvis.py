from skills.training import train
import skills.collection.MC
from neuralintents import GenericAssistant


train()


def jarvis():
    mappings = {
      "greeting": greetings,
      "shutdown": Quit
    }
    assistant = GenericAssistant('mainfolder\skills\intents.json',intent_methods=mappings, model_name="jarvis")
    assistant.train_model()
    assistant.save_model()
    


jarvis()