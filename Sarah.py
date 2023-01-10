import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import os
import cv2
import random
from requests import get
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import requests
import instaloader
import operator
import PyPDF2
import psutil
import speedtest
import datefinder
import winsound
import googletrans
import numpy as np
import urllib.request
import cv2
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
from googletrans import Translator
from PyDictionary import PyDictionary
from random import randint
from twilio.rest import Client
import screen_brightness_control as sbc
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[2].id)

# text to speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Song_seq = listdir(os.path.join("C:\Users\Mohit Shrivastava\Music\songs\YMusic"))


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning Sir!")

    elif hour >= 12 and hour < 18:
        a = "good Afternoon Sir", "Good Noon Sir"
        speak(random.choice(a))

    else:
        speak("Good evening Sir!")

    b = "I am here sir please say what you want me to do", "please tell me sir what should i help you with", "nice to see you again", "good to hear from you again", "Sir tell me how can i help you", "i am ready for your command", "i am here sir please tell me how can i help you"
    speak(random.choice(b))

# for news updates


def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c2dbde4dc0fb4e6a8bb558d39589ea08"
    main_page = requests.get(main_url).json()
    # prints main page
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eighth", "nineth", "tenth"]
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        # print(f"today's {day[1]} news is: ", head[1])
        speak(f"today's {day[i]} news is: {head[i]}")


def pdf_reader():
    book = open('Synopsis_final.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages} ")
    speak("sir please enter the page number from which i have to read")
    pg = int(input("please enter the page number : "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


def Dict(*args):
    dictionary = PyDictionary()
    speak("Activated Dictionary")
    speak("tell me the problem")
    probl = takecommand()

    if "meaning" in probl:
        probl = probl.replace("what is the ", "")
        probl = probl.replace("tell me the ", "")
        # probl = probl.replace("of ", "")
        probl = probl.replace("meaning of ", "")
        result = dictionary.meaning(probl)
        speak(f"The meaning of {probl} is {result}")

    elif "synonym" in probl:
        probl = probl.replace("what is the ", "")
        probl = probl.replace("tell me the ", "")
        # probl = probl.replace("of ", "")
        probl = probl.replace("synonym of ", "")
        result = dictionary.synonym(probl)
        speak(f"The synonym of {probl} is {result}")

    elif "antonym" in probl:
        probl = probl.replace("what is the ", "")
        probl = probl.replace("tell me the ", "")
        # probl = probl.replace("of ", "")
        probl = probl.replace("antonym of ", "")
        result = dictionary.antonym(probl)
        speak(f"The antonym of {probl} is {result}")


def alarm(text):
    dTimeA = datefinder.find_dates(text)
    for m in dTimeA:
        print(m)
    stringA = str(m)
    timeA = stringA[11:]
    hourA = timeA[:-6]
    hourA = int(hourA)
    minA = timeA[3:-3]
    minA = int(minA)

    while True:
        # print("your alarm has been set")
        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                print("your alarm is running")
                winsound.PlaySound(
                    'C:\\Music\\Timmy-turner.mp3', winsound.SND_LOOP)
            elif minA < datetime.datetime.now().minute:
                break


# speech to text

def takecommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        # speak("Say that again please!")
        # print("say that again please...")
        return "None"
    query = query.lower()
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jarvis.6283@gmail.com', 'Welcome@628')
    server.sendmail('jarvis.6283@gmail.com', to, content)
    server.close()


# if __name__ == "__main__":
def TaskExecution():

    # psw = pyautogui.password(text='Enter the password before continuing',
    #                          title='Password Protected', default='', mask='*')
    # if psw == "Mohit123":
    wishme()
    while True:
        query = takecommand().lower()

# Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube")

        elif 'open google' in query:
            speak("sir what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            # speak("opening google")

        elif "google search" in query or "search on google" in query:
            speak("This is what i found sir!")
            query = query.replace("google search", "")
            kit.search(query)

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")
            speak("stackoverflow")

        elif "facebook" in query:
            webbrowser.open("facebook.com")
            speak("opening facebook")

        elif "location" in query:
            webbrowser.open(
                "https://www.google.co.in/maps/@26.1417992,85.3624744,19.52z?hl=en&authuser=0")
            speak("getting your location")

# opening and closing applications
        elif "open notepad" in query:
            npad = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npad)
            speak("opening notepad")

        elif "close notepad" in query:
            speak("okay sir!, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open my notepad" in query:
            ynp = "C:\\Users\\Mohit Shrivastava\\AppData\\Local\\Programs\\Notepad+"
            speak("okay sir, opening your notepad")
            os.startfile(ynp)

        elif "open command prompt" in query:
            os.system("start cmd")
            speak("opening command prompt")

        elif "open camera" in query:
            cap = cv2.VideoCapture(50)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(3)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            speak("opening camera")

# changing voice
        elif "change your voice" in query or "be a boy" in query:
            engine.setProperty('voice', voices[0].id)
            speak("is it fine sir!")
            query = takecommand().lower()
            if "yes" in query:
                speak("thank you sir")
            else:
                engine.setProperty('voice', voices[2].id)
                speak("okay sir, i will be on this voice only")

        elif "default voice" in query or "talk to me in your default voice" in query or "girls voice" in query:
            engine.setProperty('voice', voices[2].id)
            speak("now is it fine sir!")
            query = takecommand().lower()
            if "yes" in query:
                speak("thank you sir")
            else:
                engine.setProperty('voice', voices[0].id)
                speak("okay sir, i will be on this voice only")

# predefined answers
        elif 'your name' in query:
            speak("My name is sarah")

        elif "your boss" in query:
            speak("i have been developed by Mohit shrivastava")

        elif "have a girlfriend" in query:
            speak("i am in relationship with wi-fi")

        elif "be my Boyfriend" in query:
            speak("Sorry! i have a girlfriend")

        elif "speak hindi" in query:
            speak("i am learning it")

        elif "who are you" in query:
            speak("I am your assistant,how may i help you")

        elif "who is harsh" in query:
            speak("He is your son")

        elif "change your name" in query:
            speak("No! sir i am Happy with my Name, Sarah")

# doing tasks
        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak("playing music")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\Mohit Shrivastava\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif "where i am" in query or "where we are" in query:
            speak("wait sir,let me check")
            try:
                ipAdd = requests.get('https://api.apify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                state = geo_data['state']
                country = geo_data['country']
                speak(
                    f"sir i am not sure, but i think we are in {state} city of {country} country")
            except Exception as e:
                speak(
                    "sorry sir, due to network issue i am not able to find where we are.")
                pass

# song on youtube
        elif "play song on youtube" in query:
            speak("which song u wanna listen to sir!")
            sn = takecommand().lower()
            kit.playonyt(f"{sn}")

# query on youtube
        elif "youtube search" in query or "search on youtube" in query or "search youtube" in query:
            speak("This is what i found for your search.")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)

        elif "search something on youtube" in query:
            speak("what should i search on youtube")
            sm = takecommand()
            kit.playonyt(f"{sm}")

        elif "full screen" in query:
            pyautogui.press("f")
        elif "exit full screen" in query:
            pyautogui.press("esc")
        elif "pause" in query:
            pyautogui.press("k")
        elif "play" in query:
            pyautogui.press("space")
        elif "restart" in query:
            pyautogui.press("0")
        elif "mute" in query:
            pyautogui.press("m")
        elif "skip" in query:
            pyautogui.press("l")
        elif "back" in query:
            pyautogui.press("j")
        elif "film mode" in query or "film mode" in query:
            pyautogui.press("t")
        elif "minimize" in query or "picture in picture" in query or "minimise" in query:
            pyautogui.press("i")

# whatsaap message

        elif "send message" in query or "send message on whatsapp" in query or "schedule a message" in query:
            speak("You need to verify yourself first")
            wpp = pyautogui.password(
                text='Enter the pin For Acessing Whatsapp', title='Password Protected', default='', mask='*')
            if wpp == "Mohit123":
                speak("Verified!")
                speak("to whom, sir!")
                query = takecommand()
                if "mohit" in query:
                    speak("what should i say, to Mohit Sir!")
                    wp = takecommand().lower()
                    speak("tell me the time sir, The hour first!")
                    hour = int(takecommand())
                    speak("Please tell me the Minute!")
                    min = int(takecommand())
                    kit.sendwhatmsg(f"+916283609508", f"{wp}", hour, min, 20)

                if "dhruv" in query:
                    speak("what should i say to Dhruv!")
                    wp = takecommand().lower()
                    speak("tell me the time sir, The hour first!")
                    hour = int(takecommand())
                    speak("Please tell me the Minute!")
                    min = int(takecommand())
                    kit.sendwhatmsg(f"+919988417321", f"{wp}", hour, min, 20)

                else:
                    speak(
                        "You need to give me the phone number,because i can't recognize this name.")
                    speak(
                        "How would you like to give me the input : Type here or speak")
                    query = takecommand()
                    if "type" in query:
                        phone = int(
                            input("Start typing from here (press enter when You finish) : "))
                        # ph = +91 + phone
                        speak("What should I say to them.")
                        wp = takecommand()
                        speak("tell me the time sir, The hour first!")
                        hour = int(takecommand())
                        speak("Please tell me the Minute!")
                        min = int(takecommand())
                        kit.sendwhatmsg(f"+91{phone}", f"{wp}", hour, min, 20)

                    if "speak" in query:
                        speak("start speaking now :")
                        phone = int(takecommand())

                        # phone = int(takecommand())
                        # ph = +91 + phone
                        speak("What should I say to them.")
                        wp = takecommand().lower()
                        speak("tell me the time sir, The hour first!")
                        hour = int(takecommand())
                        speak("Please tell me the Minute!")
                        min = int(takecommand())
                        kit.sendwhatmsg(f"+91{phone}", f"{wp}", hour, min, 20)

            else:
                pyautogui.alert(
                    text='Wrong Password', title='Warning', button='OK')
                speak("You can not access whatsapp")

# Setting an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'C:\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

# telling a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

# tasks on system
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# switching a window

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

# asking news
        elif "news" in query:
            speak("Please wait sir, fetching the news")
            news()

# booking reservation
        elif "book a reservation" in query:
            try:
                speak("for which room, and for what time sir?")
                content = takecommand().lower()
                to = "bookings@thetablemumbai.xyz"
                sendEmail(to, content)
                speak("reservation is done sir")
            except Exception as e:
                print(e)
                speak("Sorry  sir. I am not able to send this email at the moment")

# sending email
        # elif "send email to parshotam sir" in query:
        #     try:
        #         speak("what should i say")
        #         content = takecommand().lower()
        #         to = "mksmohit9122@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent to parshottam sir")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry  sir. I am not able to send this email at the moment")

# sending email with attachments
        elif "send email to parshotam sir" in query:
            speak("what should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'jarvis.6283@gmail.com'  # own email
                password = 'Welcome@628'  # own password
                send_to_email = 'parshotam.22738@lpu.co.in'  # person email id
                speak("okay sir, what is the subject for this email")
                query = takecommand().lower()
                subject = query  # the subject in the email
                speak("and sir, what is the message for this email")
                query2 = takecommand().lower()
                message = query2
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("please enter the path here")

                speak("okay sir, sending the email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                # Setup yhe attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('content-Disposition',
                                "attachment; filename = %s" % filename)

                # Attach the attachment to the MIMEMultipart object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to parshotam sir")

            else:
                email = 'jarvis.6283@gmail.com'
                password = 'Welcome@628'
                send_to_email = "parshotam.22738@lpu.co.in"
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email, message)
                server.quit()
                speak("email has been sent to parshotam sir")

        elif "send email to pratik" in query:
            speak("what should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'jarvis.6283@gmail.com'  # own email
                password = 'Welcome@628'  # own password
                send_to_email = 'prateek.ver123@gmail.com'  # person email id
                speak("okay sir, what is the subject for this email")
                query = takecommand().lower()
                subject = query  # the subject in the email
                speak("and sir, what is the message for this email")
                query2 = takecommand().lower()
                message = query2
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("please enter the path here")

                speak("okay sir, sending the email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                # Setup yhe attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('content-Disposition',
                                "attachment; filename = %s" % filename)

                # Attach the attachment to the MIMEMultipart object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to pratick")

            else:
                email = 'jarvis.6283@gmail.com'
                password = 'Welcome@628'
                send_to_email = "prateek.raj123@gmail.com"
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email, message)
                server.quit()
                speak("email has been sent to parshotam sir")

# Instagram profile
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please say the username correctly.")

            name = takecommand().lower()
            name = input("Enter the username correctly : ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            # time.sleep(3)
            speak("sir would you like to download the profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture of the user has been saved in our main folder. now i am ready for the next command")
            else:
                pass

# taking screenshot
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please hold the screen for few seconds, i am taking screenshot")
            # time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot has been saved in our main folder. now i am ready for the next command")

# try
        # elif "image to" in query:
        #     pywhatkit.image_to_ascii_art("C:\\Users\Mohit Shrivastava\\Desktop\\Major Project\\try.png", "C:\\Users\Mohit Shrivastava\\Desktop\\Major Project\\try.png")

# PDF Reader
        elif "read pdf" in query:
            pdf_reader()

# text to handwriting

        elif "text to writing" in query:
            speak("How would you like to give the input : type here or speak")
            query = takecommand().lower()
            if "type" in query:
                ip = input(
                    "Start typing from here(press enter when You finish) : ")
                kit.text_to_handwriting(f"{ip}", rgb=[0, 0, 0])
            else:
                speak("start speaking now :")
                inp = takecommand().lower()
                kit.text_to_handwriting(f"{inp}", rgb=[0, 0, 0])

        # elif "quit" in query:
        #     speak("Okay, as you say sir!")
        #     exit()

        # speak("sir, do you have any other work")

# ------------------------Hiding Files------------------------
        # elif "hide all files" in query or "hide this folder" in query:
        #     speak("are you sure, you want to hide all your files inside this folder")
        #     condition = takecommand().lower()
        #     if "yes" in condition or "Hide" in condition:
        #         os.system("attrib +h /s /d")
        #         speak("sir, all the files in this folder are now hidden.")
        #     elif "leave it" in condition or "leave for now" in condition:
        #         speak("okay sir, as you wish")

        # elif "make it visible" in query or "visible" in query or "visible for everyone" in query or "unhide" in query:
        #     speak("are you sure , you want to unhide everything in this folder")
        #     query = takecommand().lower()
        #     if "yes" in query or "unhide" in query:
        #         os.system("attrib -h /s /d")
        #         speak("sir, all the files in this folder are now visible for everyone, i wish you are taking this decision in your own peace")

            # elif "leave it" in query or "leave for now" in query:
            #     speak("okay sir, as you wish")

# Mathematical Commands
        elif "can you calculate" in query or "do calulation" in query or "do some calculation" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what u want to calculate : ")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)

            try:
                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        'divided': operator.__truediv__,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your reasult is")
                speak(eval_binary_expr(*(my_string.split())))
            except Exception as e:
                return None

# greetings
        elif "hello" in query or "hey" in query:
            speak("hello sir, may i help you with something..")

        elif "how are you" in query or "how are you doing" in query:
            speak("i am fine sir, what about you.")

        elif "also good" in query or "fine" in query:
            speak("that's great to hear from you.")

        elif "thank you" in query or "thanks" in query:
            speak("it's my pleasure sir.")

        elif "you can sleep" in query or "sleep now" in query:
            speak("okay sir, i am going to sleep now, you can call me anytime.")
            break

# Temperature
        elif "temperature" in query:
            search = "temperature in Muzaffarpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

# how to do
        elif "activate how to do" in query:
            speak("how to do, is activated")
            while True:
                speak("please tell me what you want to know.")
                how = takecommand()
                try:
                    if "exit" in how or "quit" in how or "close" in how or "leave" in how or "deactivate" in how:
                        speak("okay how to do, is now deactivated")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")

# system battery
        elif "how much power left" in query or "battery" in query or "power we have" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f" sir our system has {percentage} percent power left")
            if percentage >= 75:
                speak("we have enough power left, we can continue with our work")
            elif percentage >= 40 and percentage < 75:
                speak("we should connect our system to the charging point")
            elif percentage >= 15 and percentage < 40:
                speak(
                    "we don't have enough power left in our system, please connect to charging")
            elif percentage < 15:
                speak(
                    "we have very less power left in our system, please connect to charging as the system will shutdown very soon")

# internet speed3
        elif "speed test" in query or "internet speed" in query:
            speak("Running Network speed test")
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            dl_kb = dl/8000
            dl_mb = dl_kb/1000
            up_kb = up/8000
            up_mb = up_kb/1000
            downspkb = round(dl_kb, 2)
            downspmb = round(dl_mb, 2)
            upkb = round(up_kb, 2)
            upmb = round(up_mb, 2)
            speak(
                f"sir we have {downspkb} Kilobyte per second downloading speed and {upkb} Kilobyte per second uploading speed which is\n {downspmb} Megabyte per second downloading speed and {upmb} Megabyte per second uploading speed")

# sleep commands
        elif "hello" in query or "hey" in query:
            speak("hello sir, may i help you with something..")

        elif "how are you" in query or "how are you doing" in query:
            speak("i am fine sir, what about you.")

        elif "also good" in query or "fine" in query or "good" in query or "great" in query:
            speak("that's great to hear from you.")

        elif "thank you" in query or "thanks" in query:
            speak("it's my pleasure sir.")

        elif "you can sleep" in query or "sleep now" in query or "go to sleep" in query or "pause listening" in query:
            speak("okay sir, i am going to sleep now, you can call me anytime.")
            break

# remember
        elif "what did i tell you" in query or "do you remember" in query or "what did i told you to remember" in query:
            remember = open("data.txt", "r").read()
            speak("i remember that " + remember)

        elif "remind me" in query or "remember" in query:
            speak("tell me what i have to remember")
            query = takecommand()
            remember = open("data.txt", "w")
            # if "i" in query:
            que2 = query.replace("i", "you").replace("my", "your")
            remember.write(que2)
            remember.close()
            speak("okay sir, i'll remember that : " + que2)

        elif "what did i tell you" in query:
            remember = open("data.txt", "r").read()
            speak("i remember that " + remember)

# alarm
        elif 'alarm' in query:
            speak("for what time sir")
            ask = takecommand()
            alarm(ask)

# Entertain
        elif "bored" in query or "entertain" in query:
            speak("what would you like to do now, listen to a joke or play online game")
            query = takecommand()
            if "joke" in query:
                joke = pyjokes.get_joke()
                speak(joke)
            if "game" in query:
                webbrowser.open("http://slither.io/")

# Personalized Weather

        elif "weather outside" in query:
            try:
                # speak("please say the city you are in")
                weathercity = ("muzaffarpur")
                # weathercity = input("What city are you in? ")

                weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' +
                                       weathercity+'&appid=886705b4c1182eb1c69f28eb8c520e20')
                url = ('http://api.openweathermap.org/data/2.5/weather?q=' +
                       weathercity+'&appid=886705b4c1182eb1c69f28eb8c520e20')

                def spinning_cursor():
                    while True:
                        for cursor in '|/-\\':
                            yield cursor

                data = weather.json()

                temp = data['main']['temp']
                description = data['weather'][0]['description']
                weatherprint = "In {}, it is currently {}°C with {}."
                spinner = spinning_cursor()
                for _ in range(25):
                    sys.stdout.write(next(spinner))
                    sys.stdout.flush()
                    # time.sleep(0.1)
                    sys.stdout.write('\b')

                convert = int(temp - 273.15)
                # print(weatherprint.format(weathercity, convert, description))
                speak(weatherprint.format(weathercity, convert, description))
            except Exception as e:
                return None

# worldwide weather

        elif "worldwide weather" in query:
            try:
                speak("please say the city you are in")
                weathercity = takecommand()
                # weathercity = input("What city are you in? ")

                weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' +
                                       weathercity+'&appid=886705b4c1182eb1c69f28eb8c520e20')
                url = ('http://api.openweathermap.org/data/2.5/weather?q=' +
                       weathercity+'&appid=886705b4c1182eb1c69f28eb8c520e20')

                def spinning_cursor():
                    while True:
                        for cursor in '|/-\\':
                            yield cursor

                data = weather.json()

                temp = data['main']['temp']
                description = data['weather'][0]['description']
                weatherprint = "In {}, it is currently {}°C with {}."
                spinner = spinning_cursor()
                for _ in range(25):
                    sys.stdout.write(next(spinner))
                    sys.stdout.flush()
                    # time.sleep(0.1)
                    sys.stdout.write('\b')

                convert = int(temp - 273.15)
                # print(weatherprint.format(weathercity, convert, description))
                speak(weatherprint.format(weathercity, convert, description))
            except Exception as e:
                return None

# twitter automation
        elif "twitter" in query or "tweet" in query:
            psw = pyautogui.password(
                text='Enter the password before continuing', title='Password Protected', default='', mask='*')
            if psw == "Mohit123":
                os.system(
                    'python twitterbot.py')
            else:
                pyautogui.alert(
                    text='Wrong Password', title='Warning', button='OK')

# sending SMS
        elif "send sms to me" in query:
            speak("sir what should i say")
            msz = takecommand()
            account_sid = 'AC82cf2b1076dfe03d552c54e70afb0156'
            auth_token = 'ff769eeb7d171be8a60aff5b35245da0'

            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body=msz,
                    from_='+14079555129',
                    to='+916283609508'
                )

            print(message.sid)

        elif "send sms to gibran" in query:
            speak("sir what should i say")
            msz = takecommand()
            account_sid = 'AC82cf2b1076dfe03d552c54e70afb0156'
            auth_token = 'ff769eeb7d171be8a60aff5b35245da0'

            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body=msz,
                    from_='+14079555129',
                    to='+917009340032'
                )

            print(message.sid)

# Calling
        elif "call me" in query:
            account_sid = 'AC82cf2b1076dfe03d552c54e70afb0156'
            auth_token = 'ff769eeb7d171be8a60aff5b35245da0'

            client = Client(account_sid, auth_token)

            message = client.calls \
                .create(
                    twiml='<Response><Say>Hello sir! this is Sarah here, how are you? </Say></Response>',
                    from_='+14079555129',
                    to='+916283609508'
                )

            print(message.sid)

# Volume control
        elif "volume up" in query:
            pyautogui.press("Volumeup")

        elif "volume down" in query:
            pyautogui.press("Volumedown")

        elif "mute" in query or "volume mute" in query:
            pyautogui.press("volumemute")

# alert Box
        elif "alert" in query or "pause program" in query:
            speak("Your program will be paused until you press enter")
            pyautogui.alert(
                'Your program will be paused until you press enter.')

# Scrolling
        elif "scroll up" in query:
            pyautogui.scroll(400)   # scroll up 100 "clicks"

        elif "scroll down" in query:
            pyautogui.scroll(-400)  # scroll down 10 "clicks"

        elif "scroll" in query:
            pyautogui.scroll(10, x=100, y=100)

# Customized screenshot
        elif "customised screenshot" in query:
            speak("Select the area")
            pyautogui.hotkey('win', 'shift', 's')

# refresh system
        elif "refresh" in query:
            speak("Refreshing system")
            pyautogui.hotkey('win', 'm')
            pyautogui.press('f5')
            pyautogui.hotkey('win', 'shift', 'm')
            speak("System refreshed")

# control Brightness
        elif "set brightness to 50" in query:
            sbc.set_brightness(50)
            speak("Brightness has been set to 50%")

        elif "increase brightness by 25" in query:
            sbc.set_brightness('+25')
            speak("Brightness has been increased by 25%")

        elif "decrease brightness by 30" in query:
            sbc.set_brightness('-30')
            speak("Brightness has been decreased by 30%")

        elif "set brightness to 30" in query:
            sbc.set_brightness(30)
            speak("Brightness has been set to 30%")

        elif "set brightness to zero" in query:
            sbc.set_brightness(0)
            speak("Brightness has been set to 0%")

# password
        # elif "password" in query:
        #     password(text='', title='', default='', mask='*')

# notification checker
        elif "hide notification" in query:
            pyautogui.hotkey('win', 'a')

        elif "notification" in query or "check notification" in query:
            # speak("Here are the notifications!")
            pyautogui.hotkey('win', 'a')

# Open Browser
        elif "brave" in query:
            bravepath = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bravepath)
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'shift', 'n')

# rock paper scissor
        elif "play game" in query:
            speak("okay sir! before starting the game let me tell you how to play, you have to choose any of the three things you want to and then, after comparing you will win or loose . Note, i don't cheat.")
            # create a list of play options
            t = ["Rock", "Paper", "Scissors"]

            # assign a random play to the computer
            computer = t[randint(0, 2)]
            player = False

            while player == False:
                # set player to True
                player = input("Rock, Paper, Scissors?")
                if player == computer:
                    print("Tie!")
                elif player == "Rock":
                    if computer == "Paper":
                        print("You lose!", computer, "covers", player)
                    else:
                        print("You win!", player, "smashes", computer)
                elif player == "Paper":
                    if computer == "Scissors":
                        print("You lose!", computer, "cut", player)
                    else:
                        print("You win!", player, "covers", computer)
                elif player == "Scissors":
                    if computer == "Rock":
                        print("You lose...", computer, "smashes", player)
                    else:
                        print("You win!", player, "cut", computer)
                else:
                    print("That's not a valid play. Check your spelling!")
                # player was set to True, but we want it to be False so the loop continues
                player = False
                computer = t[randint(0, 2)]

# New Desktop
        elif "new desktop" in query:
            pyautogui.hotkey('win', 'ctrl', 'right')
        elif "previous" in query:
            pyautogui.hotkey('win', 'ctrl', 'left')

# open task manager
        elif "open task manager" in query:
            speak("Opening task manager")
            pyautogui.hotkey('ctrl', 'shift', 'esc')

# Browser Automation
        elif "close this tab" in query:
            pyautogui.hotkey('ctrl', 'w')

        elif "open new tab" in query:
            pyautogui.hotkey('ctrl', 't')

        elif "open new window" in query:
            pyautogui.hotkey('ctrl', 'n')

        elif "history" in query:
            pyautogui.hotkey('ctrl', 'h')

        elif "show download" in query:
            pyautogui.hotkey('ctrl', 'j')

        elif "tor" in query:
            pyautogui.hotkey('alt', 'shift', 'n')

        elif "find" in query:
            pyautogui.hotkey('ctrl', 'f')

        elif "print" in query:
            pyautogui.hotkey('ctrl', 'p')

# opening any website
        elif "website" in query:
            query = query.replace("website", "")
            query = query.replace(" ", "")
            web1 = query.replace("open", "")
            web2 = "https://www." + web1 + ".com"
            speak(f"okay sir opening {web2}")
            webbrowser.open(web2)

# translation
        elif "translate" in query:
            translator = Translator()
            speak("select the language you want to translate")
            print(googletrans.LANGUAGES)
            input_language = input("Enter here : ")
            speak("Select the language you want to translate into : ")
            print(googletrans.LANGUAGES)
            final = input("Enter here : ")
            speak("How would you like to give the input type or speak")
            query = takecommand()
            if "speak" in query:
                speak("Start speaking now...")
                speak_sentence = takecommand()
                text = speak_sentence
                translate = translator.translate(text, dest=final)
                speak(translate.text)
                print(translate.text)
            else:
                write_sentence = input("Type here : ")
                text = write_sentence
                translate = translator.translate(text, dest=final)
                speak(translate.text)
                print(translate.text)

# Covid Tracker
        elif "covid tracker" in query or "covid" in query:
            os.system("python covid_tracker.py")

# opening Mobile Camera
        elif "open mobile camera" in query or "open camera" in query:
            speak(
                "This Feature is password protected, please enter the pin to continue...")
            cwp = pyautogui.password(
                text='Enter the pin For Acessing Camera', title='Password Protected', default='', mask='*')
            if cwp == "Mohit123":
                speak("Verified!")

                URL = "http://192.168.43.1:8080/shot.jpg"
                while True:
                    img_arr = np.array(
                        bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow("IPWebcam", img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break

                cv2.destroyAllWindows()
            else:
                pyautogui.alert(text='Wrong Password',
                                title='Warning', button='OK')

# Google Scrapped result
        elif "what is" in query or "who is" in query or "where is" in query or "which is" in query or "what are" in query:
            query = query.replace("Sarah", "")
            query = query.replace("what is", "")
            query = query.replace("who is", "")
            query = query.replace("where is", "")
            query = query.replace("which is", "")
            query = query.replace("what are", "")
            speak("This is what i found sir")
            kit.search(query)

            try:
                result = wikipedia.summary(query, 2)
                speak(result)

            except:
                speak("Sorry sir! No Speakable data found for your search")

# youtube video downloader
        elif "download video" in query or "download youtube video" in query:
            os.system("yt-download.py")
            speak("video Downloaded")

# Stock Checker
        elif "stock" in query or "stock price" in query:
            speak("Okay sir")
            os.system("Stock_Checker_Updated.py")

# Telemedicine
        elif "not feeling well" in query or "fever" in query or "sick" in query or "medicine" in query:
            speak("Please go through these process to confirm your symptoms and get some idea about the medications you might need... ")
            os.system("Telemedicine.py")


if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission or "turn on" in permission or "activate" in permission or "sara" in permission or "start listening" in permission:
            TaskExecution()
        elif "goodbye" in permission or "switch off" in permission or "deactivate" in permission or "quit" in permission or "stop listening" in permission:
            speak("Okay sir, call me when u need something. have a good day")
            sys.exit()

# end commands

        # elif "thank you" in query or "thanks" in query:
        #     speak("its my pleasure sir")

        # elif "no thanks" in query or "no thank you" in query:
        #     speak("thanks for using me sir, have a good day.")
        #     sys.exit()

        # elif "quit" in query:
        #     speak("Okay, as you say sir!")
        #     exit()

        # speak("sir, do you have any other work")
