import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<16):
        speak("Good Afternoon")
    else:
        speak("Good Evening")   

    speak("I have Jarvis!How may i help you?")     

def takeCommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold=1
      r.energy_threshold=10
      audio=r.listen(source)

    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        

        print("Say that again please...")    
        return "None"
    return query    

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("superlikeavnika@gmail.com","Mb@22232892")
    server.sendmail("superlikeavnika@gmail.com",to,content)
    server.close()

def NewsFrom():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=06499a26dfb6405baca88834b00cdffb"
  
    # fetching data in json format 
    open=requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
    print(results)    
    speak(results) 
       

if __name__=="__main__":
    wishMe()
    if 1:
        query=takeCommand().lower()
    
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
       
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        
        elif 'open google' in query:
            webbrowser.open("google.com")    

        elif 'play music' in query:
            music_dir='D:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "mail" in query:
            try:
                speak("what should I say?")
                content=takeCommand()
                to="avnika.shah99@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e:
                speak("Sorry my friend I am not able to send this mail")    

        elif "paper" in query:
                NewsFrom()
