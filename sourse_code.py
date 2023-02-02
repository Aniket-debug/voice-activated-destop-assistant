import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib
# import pyaudio
import time
# pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline

engine = pyttsx3.init('sapi5')
# sapi5 is an API by microsoft by which we can use speech recognition and text-to-speech conversion, 
# making speech technology more accessible and robust for a wide range of applications.

voices = engine.getProperty('voices')
# print(voices) #There are two inbuilt voice packs in your system.

engine.setProperty('voice',voices[0].id)
#you can use additional voices also by simply installing them into your system.

def takeCmnd():
    # this function takes audio input from the user and return string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in') 
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please.\n")
        return "None"       
    return query    


def speak(audio):
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 160)     # setting up new voice rate

    # you can also adjust volume if you want by using 
    # "volume = engine.getProperty('volume')"
    # engine.setProperty('volume',1.0)                 - setting up volume level  between 0 and 1
   
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    curr_hour=int(datetime.datetime.now().hour)
    if(curr_hour>=0 and curr_hour<12):
        speak("Good morning sir")
    elif(curr_hour>=12 and curr_hour<18):
        speak("good afternoon sir")
    else:
        speak("good evening sir")       

    speak(" How may i help you")     

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('SENDERS_MAIL','PSWRD')
    server.sendmail('SENDERS_MAIL',to,content)
    server.close()

if __name__=="__main__":
    speak("welcome sir")    
    wishMe()
    time.sleep(1)
    while True:
        query = takeCmnd().lower()
    
        # logics as per queries.
        if ('what' in query) or ('who' in query) or ('how' in query) or('suggest' in query):
            speak("let me check sir     ")
            query = query.replace("what","")
            results = wikipedia.summary(query,sentences=2)
            speak(" i have found that ")
            speak(results)
            
        elif('open youtube' in query):
            speak("sure sir     ")        
            webbrowser.open("youtube.com")
        elif('open codechef' in query):
            speak("sure sir     ")        
            webbrowser.open("codechef.com")
        elif('open codeforces' in query):
            speak("sure sir     ")        
            webbrowser.open("codeforces.com")
        elif('open google' in query):
            speak("sure sir     ")        
            webbrowser.open("google.com")   
        elif 'play music' in query:
            music_dir = 'C:\\Users\\lenovo\\Desktop\\Mymusic'    
            songs = os.listdir(music_dir) 
            os.startfile(os.path.join(music_dir,songs[0]))  
        elif 'open vlc' in query:
            path = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe' 
            os.startfile(path)
        elif 'send an email' in query:
            try:
                speak("what's the content you want to send via your email sir")
                content = takeCmnd()
                speak("and to whom you want to send it sir")
                temp = takeCmnd().lower()
                my_dict = {'rachit':'rachitsaxenakush1@gmail.com','immortal':'ffgimmortal@gmail.com'}
                to = (my_dict[temp])
                sendEmail(to,content)
                speak("task completed succesfully")
            except Exception as e:
                speak("there as an issue occured sir, Extremly sorry for that")
                print(e)

        elif(len(query)>5):
            speak("well  i am not supposed to answer that")  