#import pyaudio
import webbrowser
import requests
from requests import get
import pyttsx3
import speech_recognition as sr
import datetime
import os
import PySimpleGUI as sg
import cv2
import pywhatkit as kit
import keyboard
import praw
import smtplib
import wikipedia
import sys
import pyjokes
import tkinter as tk
import pyautogui
import time
import operator
from bs4 import BeautifulSoup

print('hola')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[0].id)

# root = tk.Tk()
# # Set the window size
# root.geometry('200x200')
# root.title('Black Screen')
# #adding video
# root.configure(bg='red')
# root.mainloop()


# text to speech function

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

speak("Holla")

# take input from user
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am hearing...")
        r.pause_threshold=1
        audio=r.listen(source, timeout=10, phrase_time_limit=5)
    #for any errors in interpreting
    try:
        print("Recognizing")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said {query}")
    #make user repeat their command
    except Exception as e:
        speak('Please repeat..')
        return "none"
    return query
# wish me good morning/afternoon/evening
def wish():
    hour=int(datetime.datetime.now().hour)
    if (hour>=0 and hour <12):
        speak("Good Morning Sir")
    elif (hour>12 and hour<18):
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("It is %H:%M:%S")
    speak("I am Larry. How can i assist you today?")

def news():
    main_url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c06e21ec638a41df9690bcb4399016e1"
    mainpage = requests.get(main_url).json()
    articles=mainpage["articles"]
    head=[]
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"todays {day[i]} news is {head[i]}")


def sendEmail(to, email):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('advitdhaon@gmail.com', 'Advitdhaon')
    server.sendmail('advitdhaon@gmail.com', to, email)
    server.close()

def evil():
        reddit = praw.Reddit(user_agent=True, client_id = "H3ZsL1xxfiO21SzlhKpLfQ",
        client_secret="j4S02rvjmyI4HSH0yDc519URS1E-LQ" ,
        username="AdficeO" ,
        password = 'Advitdhaon')

        url = ["https://www.reddit.com/r/redditcopypasta/comments/1c99pzu/i_hate_skibidi_mewing_id_edge_to_gyat_or_rizz/" , 
           "https://www.reddit.com/r/redditcopypasta/comments/1b8zm9j/wholesome_navy_seal_copypasta/" ,
           "https://www.reddit.com/r/redditcopypasta/comments/1auqfgt/how_to_enrich_uranium/" ,
           "https://www.reddit.com/r/redditcopypasta/comments/19du8yt/indepth_fnaf_lore_explanation/" ,
           "https://www.reddit.com/r/redditcopypasta/comments/1917xro/i_love_you_anny/" ,
           "https://www.reddit.com/r/redditcopypasta/comments/15ok2vg/can_you_eat_too_much_sand/" ,
           "https://www.reddit.com/r/redditcopypasta/comments/zbgeiy/seinfeld_script_about_kramer_being_a_flatearther/" ,
           "https://www.reddit.com/r/redditcopypasta/comments/bkbz6r/steam/" ,
           "https://www.reddit.com/r/redditcopypasta/comments/agfa1k/hamburgers/" ,
           "https://www.reddit.com/r/redditcopypasta/comments/1ikvv0/gosh_im_quite_taken_aback_to_be_honest/" ,
           ]
        for link in url:
            post = reddit.submission(url=link)
            aa = (post.selftext)
            while True:
                if(keyboard.is_pressed('a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h'
                                       'i' or 'j' or 'k' or 'l' or 'm' or 'n' or 'o' or 'p'
                                       'q' or 'r' or 's' or 't' or 'u' or 'v' or 'w' or 'x'
                                       or 'y' or 'z')):
                        sound_path="C:\\Users\\advit\\Videos\\music"
                        sound=os.listdir(sound_path)
                        os.startfile(os.path.join(sound_path, sound[0]))
                        # speak(aa)
        
            

if __name__=="main_":
    wish()
    while True:
        query=takeCommand().lower()
        # print(a)
        #open notepad
        if "open notepad" in query:
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        #open cmd propt
        elif "open command prompt" in query:
            os.system("start cmd")
        #open camera
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        #to find ip address
        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your ip address is {ip}")
        #to search smth in wikipedia
        elif "wikipedia" in query:
            speak("Searching on Wikipedia..")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 10)
            speak("As per wikipedia,")
            speak(result)
            # print(result)
        #open youtube
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        #instagram
        elif "instagram" in query:
            webbrowser.open("https://www.instagram.com")
        #google docs
        elif "google docs" in query:
            webbrowser.open("https://www.docs.google.com")
        #google search
        elif "open google" in query:
            speak("Sir, what should i open on google?")
            cm = takeCommand().lower()
            cmsuper = f"https://www.google.com/search?q={cm}"
            webbrowser.open(f"{cmsuper}")
        #chatgpt
        elif "chat gpt" in query:
            webbrowser.open("https://www.chatgpt.com")
        #to send a whatsapp message
        elif "send a whatsapp message" in query:
            speak("Sir, what message should i send ?")
            msg=takeCommand().lower()
            hour=int(datetime.datetime.now().hour)
            min=int(datetime.datetime.now().minute)
            kit.sendwhatmsg("+918853670844", msg , hour, min+1)
        #play song on youtube
        elif "play a song" in query:
            speak("Sir, Which song should i play on youtube")
            sng=takeCommand().lower()
            kit.playonyt(sng)
        #for email
        elif "send email" in query:
            try:
                speak("What should i say?")
                email=takeCommand().lower()
                speak("Who should i send this email to? Please type the email address")
                to = input()
                sendEmail(to, email)
                speak("This email has been sent")
            except Exception as e:
                print(e)
                speak("I was not able to send this email, Sir")
        # elif "temperature" in query:
        #     search = "temperature in lucknow"
        #     url = f"https://www.google.com/search/q?{search}"
        #     r = requests.get(url)
        #     data = BeautifulSoup(r.text, 'html.parser')
        #     temp = data.find("div", class_= "BNeawe").text
        #     speak(f"current {search} is {temp}")
        #sussy baka
        elif "goodbye" in query:
            sound_path="C:\\Users\\advit\\Videos\\music"
            sound=os.listdir(sound_path)
            os.startfile(os.path.join(sound_path, sound[1]))
        elif "open genshin impact" in query:
            os.startfile("C:\\Program Files\\Genshin Impact\\Launcher.exe")
        elif "sleep" in query:
            speak("Thank you for using me, Sir, have a good day")
            sys.exit()
        elif "set an alarm" in query:
            speak("What time would you like to set the alarm for?")
            settime=int(input())
            ct=int(datetime.datetime.now().hour)
            if ct==settime:
                sound_path="C:\\Users\\advit\\Videos\\music"
                sound=os.listdir(sound_path)
                os.startfile(os.path.join(sound_path, sound[0]))
        elif "tell me a joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "tell me the news" in query:
            speak("Please wait sir, i am fetching the news")
            news()
        elif "where am i" in query:
            speak("Let me check where you are")
            try:
                ipaddress=requests.get("https://api.ipify.org").text
                print(ipaddress)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipaddress+'.json'
                geo_requests=requests.get(url)
                geodata=geo_requests.json()
                city = geodata['city']
                country = geodata['country']
                speak(f"I think that  you are in {city} city of the country {country}")
            except Exception as e:
                speak("I apologise, I am unable to detect the location due to network issues")
            pass
        elif "take a screenshot" in query:
            speak("Please wait Sir, I am running the screenshot software")
            time.sleep(5)
            img = pyautogui.press("prtsc")
            # name = takeCommand().lower
            # img.save(f"{name}.png")
            # speak("The image has been saved in the main folder")

        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif "evil" in query: 
            evil()
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("What do you want me to calculate")
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    'divide': operator._truediv_
                }[op]
            def eval_binaryexpression(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("The result is")
            speak(eval_binaryexpression(*(my_string.split())))
        elif "hello" in query:
            speak("Hello Sir, How are you?")
        elif "good" in query:
            speak("I am also good Sir, What about you?")
        elif "filmora" in query:
            path = "C:\\Users\\advit\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Wondershare\\Wondershare Filmora\\Wondershare Filmora 13.lnk "
            os.startfile(path)
        elif "minecraft" in query:
            path = "C:\\Users\\advit\\Downloads\\MinecraftInstaller.exe"
            os.startfile(path)
        elif "microsoft edge" in query:
            path ="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"
            os.startfile(path)
        elif "canva" in query:
            os.startfile("c:\\Users\\advit\\OneDrive\\Desktop\\Canva.lnk")
        # elif "pdf reader" in query:
        #     pdf_reader()