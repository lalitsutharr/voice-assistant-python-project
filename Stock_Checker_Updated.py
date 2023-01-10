import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
from time import ctime  # get time details
import webbrowser  # open browser
# import ssl
# import certifi
import time
import os  # to remove created audio files
# import subprocess
import pyttsx3
import bs4 as bs
import urllib.request
import requests
import yfinance as yf


class person:
    name = ''

    def setName(self, name):
        self.name = name


class asis:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()  # initialise a recogniser
# listen for audio and convert it to text:


def record_audio(ask=""):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            # error: recognizer is not connected
            engine_speak('Sorry, the service is down')
        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()

# get string and make a audio file to be played


def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print(asis_obj.name + ":", audio_string)  # print what app said
    os.remove(audio_file)  # remove audio file


def respond(voice_data):
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name,
                     "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings)-1)]
        engine_speak(greet)

     # 7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.lower().split(" of ")[-1].strip()
        stocks = {
            "apple": "AAPL",
            "microsoft": "MSFT",
            "facebook": "FB",
            "tesla": "TSLA",
            "bitcoin": "BTC-USD"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]

            engine_speak(
                f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
        except:
            engine_speak('oops, something went wrong')

    if there_exists(["exit", "quit", "goodbye", "exit stock checker"]):
        engine_speak("bye")
        exit()


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'sara'
person_obj.name = ""
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Recording")  # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data)  # respond
