import pyttsx3 # pip install ppytsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia as wikipedia_ #pip install wikipedai
import webbrowser as wb
import random
import os
import smtplib
import requests
from pprint import pprint
from selenium import webdriver #pip install selenium
from subprocess import Popen, PIPE
import requests
import pyjokes
import psutil

engine = pyttsx3.init()
engine.setProperty('rate', 180)     # setting up new voice rate
engine.setProperty('volume', 1.0)   # settin up the volume
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for male , 0 for female

my_gmail = 'i0562269690@gmail.com'
my_password = 'mcali2005'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M")
    speak(Time)

def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def weather():
    
    url = r"http://api.openweathermap.org/data/2.5/weather?q=Dammam&units=metric&appid=c4d1611172e2ceb1fd647205304d2adc"
    response = requests.get(url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        i = x["wind"]
        current_windspeed = i["speed"]
        current_winddeg = i["deg"]
        j = x["clouds"]
        current_cloudiness = j["all"]
        u = (current_cloudiness, 'percent')
        speak("the current weather is")
        speak(weather_description)
        speak("the current temperature is")
        speak(current_temperature)
        speak("the current clouds percentage in the air is")
        speak(u)
    else:
        speak("eror404")
        

def wishme():
    speak("welcome back")
    skip = wakecommand().lower()
    if 'skip' in skip:
        return
    elif 'next' in skip:
        return
    speak("the current time is")
    time()
    skip = wakecommand().lower()
    if 'skip' in skip:
        return
    elif 'next' in skip:
        return
    weather()
    skip = wakecommand().lower()
    if 'skip' in skip:
        return
    elif 'next' in skip:
        return
    hour = datetime.datetime.now().hour
    if hour >= 24 and hour < 11:
        speak("good morning sir!. this is your A.I. assistant . please tell me how can I help you?")
    elif hour >= 11 and hour < 16:
        speak("good afternoon sir!. this is your A.I. assistant . please tell me how can I help you?")
    else:
        speak("good evening sir!. this is your A.I. assistant . please tell me how can I help you?")

    
def wakecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    
    query = r.recognize_google(audio, language='en-US')
    print(query)
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(my_gmail, my_password)
    server.sendmail(my_gmail, to, content)
    server.close()




def check_my_code(py_filename):
  
  
    def get_path():
   
       pythonfile = py_filename

  
       for root, dirs, files in os.walk(r'C:\Users\GAMER\Desktop'):
        for name in files:
        
           # As we need to get the provided python file, 
           # comparing here like this
           if name == pythonfile:  
               new_path = os.path.abspath(os.path.join(root, name))
               return new_path
  
    new_path = "python " + get_path()

    def execute_return(cmd):
        args = cmd.split()
        proc = Popen(args, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        return out, err
  
    def mak_req(error):
        resp = requests.get("https://api.stackexchange.com/" +
                        "/2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
        return resp.json()

    def get_urls(json_dict):
       url_list = []
       count = 0
      
       for i in json_dict['items']:
        if i['is_answered']:
            url_list.append(i["link"])
        count += 1
        if count == 3 or count == len(i):
            break
      
       for i in url_list:
            wb.open(i)
      
       for i in url_list:
            wb.open(i)

    out, err = execute_return(new_path)

    erro = err.decode("utf-8").strip().split("\r\n")[-1]
    print(erro)

    if erro:
       filter_error = erro.split(":")
       json1 = mak_req(filter_error[0])
       json2 = mak_req(filter_error[1])
       json = mak_req(erro)
       get_urls(json1)
       get_urls(json2)
       get_urls(json)

    else:
       print("No error")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)




def joke():
    speak(pyjokes.get_joke())

def playmusic():
            wb.register('chrome',
  	         None,
  	         wb.BackgroundBrowser(r"C:\Users\GAMER\AppData\Local\Google\Chrome\Application\chrome.exe"))
            rand = random.randint(0,98)
            wb.get('chrome').open(r"https://www.youtube.com/watch?v=BylkQHFemTw&list=PLXBkpQDrA97_NWutYvrEygFnueuZ_VvJq&index={}".format(rand))

 
def Quit():
    speak("ok sir shutting down the system")
    quit()

def wikipedia():
    try:
     speak('what should a search')
     query = wakecommand().lower()
     results = wikipedia_.summary(query, sentences = 2)
     speak("According to Wikipedia")
     print(results)
     speak(results)
     url = wikipedia_.page(query).url
     print("if you want to learn more visit {}".format(url))
    except Exception as e:
     speak("couldn't find that sir")
    


def chorme():
    speak("what should i search or open for you sir?!")
            
            

    r = sr.Recognizer()

    with sr.Microphone() as source:
     print('say something!')
     audio = r.listen(source)
     print("done")
    try:
     text = r.recognize_google(audio)
     print('google think you said:\n' +text)
     text = text.replace(' ', '+')
     wb.register('chrome',
	 None,
	 wb.BackgroundBrowser(r"C:\Users\GAMER\AppData\Local\Google\Chrome\Application\chrome.exe"))
     wb.get('chrome').open("https://www.google.com.tr/search?q={}".format(text))
    except Exception as e:
     print(e)


def netflix():
    wb.register('chrome',
	None,
	wb.BackgroundBrowser(r"C:\Users\GAMER\AppData\Local\Google\Chrome\Application\chrome.exe"))
    wb.get('chrome').open(r"https://www.netflix.com/browse")


def spiller():
    speak("what is the word you want to spell")
    query = wakecommand().lower()
    
    spill = list(query)

    speak(spill)


def run_alexa():
    wishme()
    while True:
        query = takecommand().lower()



        if 'search in wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search in wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            


        elif 'a joke' in query:
            joke()

        elif 'check my cpu' in query:
            cpu()
        
        elif 'music' in query:
            if "play" in query:
                playmusic()
            else:
                speak("Did you mean 'play music'?")
                print("Say something - Yes or No")
                query = takecommand().lower()
                if "yes" in query:
                    playmusic()

            
            

        elif 'search chrome' and 'search google' in query:
            speak("what should i search or open for you sir?!")
            
            

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print('say something!')
                audio = r.listen(source)
                print("done")
            try:
                text = r.recognize_google(audio)
                print('google think you said:\n' +text)
                text = text.replace(' ', '+')
                wb.register('chrome',
	            None,
	            wb.BackgroundBrowser(r"C:\Users\GAMER\AppData\Local\Google\Chrome\Application\chrome.exe"))
                wb.get('chrome').open("https://www.google.com.tr/search?q={}".format(text))
            except Exception as e:
                print(e)
        
        elif 'how is the weather' in query:

            weather()


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'play netflix' in query:
            wb.register('chrome',
	        None,
	        wb.BackgroundBrowser(r"C:\Users\GAMER\AppData\Local\Google\Chrome\Application\chrome.exe"))
            wb.get('chrome').open(r"https://www.netflix.com/browse")

        
        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)


        elif 'send an email' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ReciversEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")      

        elif 'open code' in query:
            codePath = "C:\\Users\\user account\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"#ADD THE PATH OF THE PROGEM HERE
            os.startfile(codePath)


        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))
        
        elif 'go offline' in query:
            speak("ok sir the system is going into rest mode")
            run_wake()

        elif 'shutdown' in query:
            speak("ok sir shutting down the system")
            quit()


def run_wake():
    while True:
        wakeup = wakecommand().lower()
        if 'hey MC' in wakeup:
            while True:
                run_alexa()
        elif 'hi MC' in wakeup:
            while True:
                run_alexa()  
        elif 'hey jarvis' in wakeup:
            while True:
                run_alexa()
        elif 'shutdown' in wakeup:
            speak("ok sir shutting down the system")
            quit()