
# length = int(input("Enter the length : "))
# breadth = int(input("Enter the breadth : "))

# if length == breadth:
#     print("it is a square.")
# else:
#     print("it is a rectangle.")


# sum = 0
# for i in range(1, 5):
#     sum += i+1
# print(sum)


# L1 = [1, 2, 3, 4, 5]
# print(L1[2:-1])
# for i in range(10):
#     print(i)


# i = 10
# if (i > 15):
#     print("i is less than 15")
# else:
#     print("i am not in f")

# for i in range(1, 5):
#     print(i)

# def hello(x):
#     x = 45
#     print(x)
#     return


# x = 13
# hello(x)
# print(x)


# def add(a, b):
#     return a*b


# print(add_doc_)

# print(add(10, 20))


# UserInp = str(input("Enter a sring at least 3 char long: "))
# leng = len(UserInp)
# if leng > 2:
#     if UserInp[-3:] == 'ing':
#         UserInp += 'ly'
#     else:
#         UserInp += 'ing'
# print(f"{UserInp}")

# if str1[-3:] == 'ing':

# print("What you want to change : ")
# print("a. Celsius to Farenhiet.")
# print("b. Farenheit to celsius.")
# choice = input("Enter your choice : ")
# if 'a' in choice:
#     c = int(input("enter the temperature in celsius : "))
#     f = 9.0/5.0 * c + 32
#     print(f"{f}")
# elif 'b' in choice:
#     d = int(input("Enter the temperature in Farenhiet : "))
#     g = (d - 32) * 5.0/9.0
#     print(f"{g}")
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]

# for element in list1:
#     if element in list2:
#         print("true")

# for i in range(1, 5):
# a = i**2
# a += 1
#     list1.append(i**2)
# print(list1)
# list2 = []
# list3 = []
# for i in list1:
#     if (i % 2 == 0):
#         list2.append(i)
#     else:
#         list3.append(i)
# print(f"list2 {list2}")
# print(list3)
# for i in range(1, 40):
#     if (i % 7 == 0 and i % 5 != 0):
#         print(i)

# def splitevenodd(A):
#     evenlist = []
#     oddlist = []
#     for i in A:
#         if (i % 2 == 0):
#             evenlist.append(i)
#         else:
#             oddlist.append(i)
#     print("Even lists:", evenlist)
#     print("Odd lists:", oddlist)

# largest = list[0]
# for x in list:
#     if x > largest:
#         largest = x
# print(largest)

# list1 = ["avc", "xyz", "cfd", "hgv"]
# list1.sort()
# print(list1)
# for i in list1:
#     print
# for i in list1:
#     for list1 in range[-1:0]
#     print(i)

# def fib(mymax):
#     a, b = 0
#     while True:
#         c = a+b
#         if c < mymax
#         print("before yield keyword")
#         yield c
#         print("after yield keyword")
#         a = b
#         b = c
#         elif:
#             break

# def bubbleSort(array):

#     for i in range(len(array)):
#         for j in range(0, len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 (array[j], array[j + 1]) = (array[j + 1], array[j])


# data = [50, 15, 6, 5, 22, 81, 9]
# bubbleSort(data)
# print('Sorted Array in Asc ending Order:')
# print(data)


# import requests
# import time
# import sys

# weathercity = input("What city are you in? ")
# weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' +
#                        weathercity+'&appid=886705b4c1182eb1c69f28eb8c520e20')
# url = ('http://api.openweathermap.org/data/2.5/weather?q=' +
#        weathercity+'&appid=886705b4c1182eb1c69f28eb8c520e20')


# def spinning_cursor():
#     while True:
#         for cursor in '|/-\\':
#             yield cursor


# data = weather.json()

# temp = data['main']['temp']
# description = data['weather'][0]['description']
# weatherprint = "In {}, it is currently {}°C with {}."
# spinner = spinning_cursor()
# for _ in range(25):
#     sys.stdout.write(next(spinner))
#     sys.stdout.flush()
#     time.sleep(0.1)
#     sys.stdout.write('\b')

# convert = int(temp - 273.15)
# print(weatherprint.format(weathercity, convert, description))


# Q1
# l = [1, 2, 3, 4, 5]
# c = 1
# for i in l:
#     c = c*i
# print(c)

# q2
# for i in range(2, 41):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i)

# def odd_even(default):
#     odd_li = []
#     even_li = []
#     for i in default:
#         if (i % 2 == 0):
#             even_li.append(i)
#         else:
#             odd_li.append(i)
#     print(f"Even Elements are : {even_li}")
#     print(f"Odd Elements are : {odd_li}")


# default = []
# default1 = input("enter the list")
# default.append(default1)
# odd_even([1, 2, 3, 4, 5, 6, 7, 8])

# k, j = "Mohit", "kumar"
# print(k[2:3])
# print(j)
# k = "this is mohit\"s \v pen"
# print(k)

# k = %s("mohit")
# print(k)
# where = ("kedarnath")
# speed = ("99kmph")
# print("On your journey to %s, you drove at an average speed of %s miles per hour." % (
#     where, speed))


# print("On your journey to {where}, you drove at an average speed of {speed} miles per hour.".format(
#     where="Kedarnath", speed="99kmph"))
# s = set()
# s.add(5)
# s.add(10)
# print("Adding 5 and 10 in set", s)
# s.pop()
# print(s)

# l = []
# l.append(5)
# l.append(10)
# print(l)
# l.pop()
# print(l)
# s = set()
# print(type(s))

# k = {[f] = "mk", [h] = 'kk', [l] = "ll"}
# print(k)

# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
# print(reverse("abcd"))

# def reve(s):
#     st = ""
#     for i in
# s = "abcd"
# print(reverse("abcd"))

# print("The original string  is : ", end="")
# print(s)

# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))
# def finding(l, f):
#     for i in l:
#         if f == i:
#             return f

# print(finding([1, 2, 3, 4, 5], 4))


# print(finding([1, 2, 3, 4, 5], 5))

# write a python function to count number of strings where the length of the string is 2 or more
# def counting(s):
#     count = 0
#     for i in s:
#         if len(i) >= 2:
#             count += 1
#     return count


# print(counting(["mohit", "jlk", "mkmk", "k"]))

# a = ("check")*3
# print(a)
# x = ['ab', 'cd']
# print(len(list(map(list, x))))
# print(x)
# m = "mohit "
# k = m*2
# print(k)
# k = str(input("enter heree : "))
# print(k)
# k = 123
# h = (str(k))
# print(type(h))
# for i in range(2):
#     print("x")
# this = list((1, 2, 3, 4))
# print(type(this))
# thisset = set{“apple”, “banana”, “cherry”}
# print(type(thisset))
# myset = {“apple” , “banana”, “cherry”}
# print(type(myset))

# c = """  kdgwefkwuehf
# wefkj wejfgwekf
# wefkgwekfgwekfwe """
# print(c)
# c = 5//2
# print(c)
# a = ("check")*3
# print(a)
# def myfun(text, num):
#     while num > 0:
#         num = num - 1
#     num = 4

# num = 4

# print(myfun("Hello", num))


# def myfun(text, num):
#     while num > 0:
#         num = num - 1
#     return num


# print(myfun("Hello", num))

# print(num)
# for i in range(0, 2, -1):
#     print("hello")
# x = 1
# while (x <= 5):
#     x + 1
#     print(x)
# while (3):
#     print(2)
# x = 0
# def add_one(x):
#     x = x+1
#     return x

# add_one(1)
# print(f"x= {x}")
# my_tuple = ("p","r")
# tupl = ([2, 3], "abc", 0, 9)
# tupl[0][1] = 6
# print(tupl)
# def fn(a):
#     print(a)
# x = 90
# fn(x)
# x = 1
# while(x <= 5):
#     x + 1
#     print(x)
# a = 1
# while True:
#     if a % 7 == 0:
#         break
#     print(a)
#     a += 1
# list1 = [1, 3, 5, 4, 6, 2]
# list1.remove(3)
# print(sum(list1))
# int = 3
# print(int)
# String = "This is string slicing"
# print(String)
# print(String[2:-2])
# String = "Put some pizza sauce?"
# print(String[5:14])
# String = "Updating this string.."
# print(String)
# print(String[:5] + 'ed String')
# a = 'Joey '
# b = 'Chandler'
# print(a + b)
# a = ['Python', 'Java', 'R']
# print(a[0], a[1], a[2])
# print(4 ^ 12)
# def eve():
#     f = []
#     # a, b = 4, 30
#     for i in range(4, 31):

#         # f = []
#         if i % 2 == 0:
#             f.append(i)
#             print(f)


# print(eve())
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#     # a = n * factorial(n-1)
#     # return a


# n = int(input("Input a number to compute the factiorial : "))
# print(factorial(n))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def even_out():
#     l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     e = []
#     for i in l:
#         if i % 2 == 0:
#             l.remove(i)
#             # e.append(i)
#         return(l)


# print(even_out())


# def even_out():
#     l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     e = []
#     for i in l:
#         if i % 2 != 0:
#             e.append(i)
#         print(e)


# print(even_out())
# def palindrome(f):
#     if f == f[::-1]:
#         print("yes")
#     else:
#         print("No")
#     return f
# return f == f[::-1]


# f = "madam"
# yes = palindrome(f)
# if yes:
#     print("yes")
# else:
#     print("No")
#     c = ""
#     for i in f:
#         c + "i"
#     print(c)
# print(palindrome("madam"))


# def employee(Name, salary=9000):
#     print(Name)
#     print(salary)
#     # return Name
#     #  salary


# print(employee("Mohit", 8000))
# print(employee("Aman"))
# num = 1

# def oddl(l):
#   for i in l:
#         if i % 2 != 0:
#             print(i, end=' ')


# l = [3, 7, 8, 9, 10, 12]
# print(oddl(l))

# def func():
#     num = num + 3
#     print(num)


# func()
# print(num)

# print("Happy New Year".split())
# try:
#     a = [1, 2, 3]
#     print(a[4])
# except Exception as e:
#     print("the array is out of range")
# def errorhand(a, b):
#     try:
#         c = a-b
#         d = a+b
#         f = c/d
#         print(f)
#         if d == 0:
#             except ZeroDivisionError:
#                 print("cannot divide by zero")

# print(errorhand(2, 6))

# try:
#     print(c)
#     print(c/0)
# except (ZeroDivisionError, NameError):
#     print("your errors has been resolved")
# finally:
#     print("you are ready to go")

# def foo():
#     try:
#         return 1
#     finally:
#         return 2


# k = foo()
# print(k)

# try:
#     1/0
# except:
#     print("execption")
# else:
#     print("else")
# finally:
#     print("finally")

# try:
#     if '2' != 2:
#         raise ValueError
#     else:
#         print("same")
# except ValueError:
#     print("ValueError")
# except NameError:
#     print("NameError")
# try:
#     print("try")
# except ValueError:
#     print("ValueError")
# finally:
#     print("finally")
# def getm(m):
#     if m < 1 or m > 12:
#         raise
#     ValueError("Invalid")
#     print(m)
# getm(6)

# def fact(a):
#     factorial = 1
#     try:
#         for i in range(1, a+1):
#             factorial = factorial*i
#             print(factorial)
#     except AssertionError:
#         print("Value is negative")


# print(fact(-9))

# import pyautogui
# pyautogui.keyUp('fn')
# pyautogui.press('f7')
# psw = pyautogui.password(text='Enter the password before continuing',
#                          title='Password Protected', default='', mask='*')
# print(psw)
# pyautogui.hotkey('win', 'm')
# pyautogui.press('f5')
# pyautogui.press('f5')

# pyautogui.hotkey('win', 'm')
# pyautogui.press('f5')
# pyautogui.hotkey('win', 'shift', 'm')

# import screen_brightness_control as sbc

# set brightness to 50%
# sbc.set_brightness(20)

# set brightness to 0%
# sbc.set_brightness(0, force=True)

# increase brightness by 25%
# sbc.set_brightness('+25')

# decrease brightness by 30%
# sbc.set_brightness('-30')

# set the brightness of display 0 to 50%
# sbc.set_brightness(50, display=0)

# try:
#     m = 1500

#     if m < 2000:
#         raise ValueError(
#             "Enter the money to the amount within the given range")
#     else:
#         print("you can withdraw the amount")
# except ValueError:
#     print("execption has been handled")
# def coounting(s):
#     # str = input("Enter a string: ")
#     upper = 0
#     lower = 0
#     for i in range(len(s)):
#         # to lower case letter
#         if(s[i] >= 'a' and s[i] <= 'z'):
#             lower += 1
#         # to upper case letter
#         elif(s[i] >= 'A' and s[i] <= 'Z'):
#             upper += 1
#     print('Lower case letters= ', lower)
#     print('Upper case letters=', upper)

# print(coounting("MohIT Is YOUR boss"))

# from random import randint

# create a list of play options
# t = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
# computer = t[randint(0, 2)]

# # set player to False
# player = False

# while player == False:
#     # set player to True
#     player = input("Rock, Paper, Scissors?")
#     if player == computer:
#         print("Tie!")
#     elif player == "Rock":
#         if computer == "Paper":
#             print("You lose!", computer, "covers", player)
#         else:
#             print("You win!", player, "smashes", computer)
#     elif player == "Paper":
#         if computer == "Scissors":
#             print("You lose!", computer, "cut", player)
#         else:
#             print("You win!", player, "covers", computer)
#     elif player == "Scissors":
#         if computer == "Rock":
#             print("You lose...", computer, "smashes", player)
#         else:
#             print("You win!", player, "cut", computer)
#     else:
#         print("That's not a valid play. Check your spelling!")
#     # player was set to True, but we want it to be False so the loop continues
#     player = False
#     computer = t[randint(0, 2)]
# pyautogui.hotkey('win', 'ctrl', 'right')

# Even Roll Q1
# def show(name, age=22):
#     print(name)
#     print(age)


# n = input("Enter your name : ")
# a = int(input("Enter your age : "))
# print(show(n, a))
# print(show(n))

# Q2
# def fact(a):
#     factorial = 1
#     for i in range(1, a+1):
#         factorial = factorial*i
#         print(factorial)

# print(fact(4))
# import cv2
# import numpy as np
# import pyautogui

# cap = cv2.VideoCapture(1)

# yellow_lower = np.array([22, 93, 0])
# yellow_upper = np.array([45, 255, 255])
# prev_y = 0

# while True:
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
#     contours, hierarchy = cv2.findContours(
#         mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     for c in contours:
#         area = cv2.contourArea(c)
#         if area > 300:
#             x, y, w, h = cv2.boundingRect(c)
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#             if y < prev_y:
#                 pyautogui.press('space')

#             prev_y = y
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(10) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# chrome dino hack
# runner.instance_.gameover = () => {}
# import PyPDF2
# import pyttsx3

# book = open('Learn Python the Hard Way ( PDFDrive ).pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages
# print(pages)
# # speak(f"Total number of pages in this book {pages} ")
# speaker = pyttsx3.init()
# # speak("sir please enter the page number from which i have to read")
# # pg = int(input("please enter the page number : "))
# page = pdfReader.getPage(8)
# text = page.extractText()
# speaker.say(text)
# speaker.runAndWait()

# phone = 6283
# ph = '+91' + phone
# print(f"+91{phone}")

# class Employee:
#     def Emp_name(self):
#         print("Sarah wesley")


# fname = Employee()
# fname.Emp_name()


# class student_info:
#     def __init__(self, f, last, marks):

#         self.f = f
#         self.last = last
#         self.marks = marks
#         self.email = last+"_"+f+"@jhs.in"


# student_1 = student_info("John", "doe", 80)
# student_2 = student_info("Karen", "Page", 86)

# print(student_1.f)
# print(student_2.email)


# import googletrans
# from googletrans import Translator
# translator = Translator()

# text = '''सभी को मेरा नमस्कार! मेरा नाम हर्ष है और मैं 25 साल का हूं. अपनी पढ़ाई पूरी कर चुका हूं और अब मैं जॉब की तलाश में हूं.
# दैनिक अंग्रेजी वाक्य का उपयोग करें हिंदी अर्थ के साथ'''

# dt = translator.detect(text)
# print(dt)

# translate = translator.translate(text, dest="en")

# # translated = translator.translate(text)

# print(translate.text)

# elif "translate" in query:
# translator = Translator()
# print("select the language you want to translate")
# print(googletrans.LANGUAGES)
# input_language = input("Enter here : ")
# print("Select the language you want to translate into : ")
# print(googletrans.LANGUAGES)
# final = input("Enter here : ")
# write_sentence = input("Type here : ")
# text = write_sentence
# translate = translator.translate(text, dest=final)
# print(translate.text)

# speak("How would you like to give the input type or speak")
# if "speak" in query:
#     speak_sentence = takecommand()
#     text = speak_sentence
#     translate = translator.translate(text, dest={final})
#     speak(translate.text)
# elif "type" in query:
#     write_sentence = takecommand()
#     text = write_sentence
#     translate = translator.translate(text, dest={final})
#     speak(translate.text)


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# name = input("Enter your username: ")
# passW = input("Enter your password: ")

# driver = webdriver.Chrome(
#     executable_path="C://Users//Downloads//chromedriver.exe")


# class InstaBot():
#     def __init__(self, userName, passWord):
#         self.userName = userName
#         self.passWord = passWord

#     def login(self):
#         driver.get("https://www.instagram.com")

#         elemUser = driver.find_element_by_xpath(
#             '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
#         elemUser.send_keys(self.userName)

#         elemPass = driver.find_element_by_xpath(
#             '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
#         elemPass.send_keys(self.passWord)


# ankur = InstaBot(name, passW)
# ankur.login()


# def typeerr(j):
#     n = [1,2,3,4,5]
#     raise TypeError("only integer are allowed")


# print(typeerr(1))


# try:
#     c = 3
#     b = c/0
#     c = i + 2
# except (ZeroDivisionError, ValueError):
#     print("your errors has been resolved")
# finally:
#     print("you are ready to go")

# Python program to check if year is a leap year or not

# year = 2000


# def leap(year):
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 print("{0} is a leap year".format(year))
#             else:
#                 print("{0} is not a leap year".format(year))
#         else:
#             print("{0} is a leap year".format(year))
#     else:
#         print("{0} is not a leap year".format(year))


# print(leap(2001))


# def leapy(year):
#     if year % 4 == 0 and year % 100 != 0:
#         print(year, "is a Leap Year")
#     elif year % 100 == 0:
#         print(year, "is not a Leap Year")
#     elif year % 400 == 0:
#         print(year, "is a Leap Year")
#     else:
#         print(year, "is not a Leap Year")


# print(leapy(2001))
# def leap(year):
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 print("{0} is a leap year". format(year))
#     else:
#         print("{0} is not a leap year". format(year))


# print(leap(2001))

# from time import Ctime
# print(Ctime)

# from datetime import datetime

# now = datetime.now()

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

# def coounting(s):
# upper = 0
# lower = 0
# for i in range(len(s)):
#     if(s[i] >= 'a' and s[i] <= 'z'):
#         lower += 1
#     elif(s[i] >= 'A' and s[i] <= 'Z'):
#         upper += 1
# print('Lower case letters= ', lower)
# print('Upper case letters=', upper)

# print(coounting("HellO WORld"))

# Class
# class rectangle:
# def __init__(self,l,b):


# class circle:
#     def __init__(self, r, pie=3.14):
#         self.radius = r
#         self.pie = pie

#     def perimeter(self):
#         return 2*self.pie*self.radius

#     def area(self):
#         return self.pie*self.radius*self.radius


# cir = circle(5)
# print(cir.perimeter())
# print(cir.area())


# class addition:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         return self.num1+self.num2


# addn = addition(2, 3)
# print(addn.add())

# class Employee:
#     def __init__(self, Emp_name, Emp_age, Emp_salary):
#         self.Emp_name = Emp_name
#         self.Emp_age = Emp_age
#         self.Emp_salary = Emp_salary

#     def annual_salary(self):
#         return self.Emp_salary*12


# emp = Employee("Sarah", 21, 19000)
# print(emp.Emp_name)
# print(emp.Emp_age)
# print(emp.annual_salary())

# class Person:
#     def __init__(self, First_name, Last_name):
#         self.First_name = First_name
#         self.Last_name = Last_name

#     def printname(self):
#         print(self.First_name, self.Last_name)


# class Child(Person):
#     pass


# x = Child("Mohit", "Shrivastava")
# print(x.printname())

# s = "python rocks"
# print(s[1]*s.index("n"))
# from PyDictionary import PyDictionary
# dictionary = PyDictionary()

# probl = input("Enter the problem here: ")
# probl = probl.replace("Enter the problem here: ", "")
# probl = probl.replace("what is the ", "")
# probl = probl.replace("tell me the ", "")
# probl = probl.replace("of ", "")
# probl = probl.replace("antonym of ", "")
# result = dictionary.antonym(probl)
# print(result)
# print(f"The antonym of {probl} is {result}")

# from PyDictionary import PyDictionary
# dictionary = PyDictionary()
# print(dictionary.synonym("Book"))

# if there_exists(["price of"]):
# import yfinance as yf
# import ssl

# search_term = input("")
# search_term = search_term.lower().split(" of ")[-1].strip()
# stocks = {
#     "apple": "AAPL",
#     "microsoft": "MSFT",
#     "facebook": "FB",
#     "tesla": "TSLA",
#     "bitcoin": "BTC-USD"
# }
# try:
#     stock = stocks[search_term]
#     stock = yf.Ticker(stock)
#     price = stock.info["regularMarketPrice"]

#     print(
#         f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
# except:
#     print('oops, something went wrong')

# if there_exists(["exit", "quit", "goodbye"]):
#     speak("going offline")
#     exit()

# if there_exists(["pollution"]):
#     search_term = voice_data.split("for")[-1]
#     url = "https://weather.com/en-IN/forecast/air-quality/l/8942645b881fd43fc86ed2d932370e550513245460cabb6a48b38a3089406d92"
#     webbrowser.get().open(url)
#     engine_speak("Here is what i found for the google")
# import re
# str = "Sandeep Saradhi"
# x = re.search("Sandeep", str)
# print(x.string)
# search_term = "price of tesla"
# search_term = search_term.lower().split(" of ")[-1].strip()
# print(search_term)


# str = "Sandeep Saradhi"
# x = re.sub("S", "R", str)
# print(x)

import requests
import json
import pyttsx3
# import speech_recognition as sr
import re
import threading
import time

API_KEY = "tVQG9LhBPPNw"
PROJECT_TOKEN = "tRAsYGofNdNo"
RUN_TOKEN = "t5TvGMij1bQk"


class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.data = self.get_data()

    def get_data(self):
        response = requests.get(
            f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
        data = json.loads(response.text)
        return data

    def get_total_cases(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Coronavirus Cases:":
                return content['value']

    def get_total_deaths(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Deaths:":
                return content['value']

        return "0"

    def get_country_data(self, country):
        data = self.data["country"]

        for content in data:
            if content['name'].lower() == country.lower():
                return content

        return "0"

    def get_list_of_countries(self):
        countries = []
        for country in self.data['country']:
            countries.append(country['name'].lower())

        return countries

    def update_data(self):
        response = requests.post(
            f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run', params=self.params)

        def poll():
            time.sleep(0.1)
            old_data = self.data
            while True:
                new_data = self.get_data()
                if new_data != old_data:
                    self.data = new_data
                    print("Data updated")
                    break
                time.sleep(5)

        t = threading.Thread(target=poll)
        t.start()


def main():
    print("Started Program")
    data = Data(API_KEY, PROJECT_TOKEN)
    END_PHRASE = "stop"
    country_list = data.get_list_of_countries()

    TOTAL_PATTERNS = {
        re.compile("[\w\s]+ total [\w\s]+ cases"): data.get_total_cases,
        re.compile("[\w\s]+ total cases"): data.get_total_cases,
        re.compile("[\w\s]+ total [\w\s]+ deaths"): data.get_total_deaths,
        re.compile("[\w\s]+ total deaths"): data.get_total_deaths
    }

    COUNTRY_PATTERNS = {
        re.compile("[\w\s]+ cases [\w\s]+"): lambda country: data.get_country_data(country)['total_cases'],
        re.compile("[\w\s]+ deaths [\w\s]+"): lambda country: data.get_country_data(country)['total_deaths'],
    }

    UPDATE_COMMAND = "update"

    while True:
        # print("Listening...")
        text = input("")
        # print(text)
        result = None

        for pattern, func in COUNTRY_PATTERNS.items():
            if pattern.match(text):
                words = set(text.split(" "))
                for country in country_list:
                    if country in words:
                        result = func(country)
                        break

        for pattern, func in TOTAL_PATTERNS.items():
            if pattern.match(text):
                result = func()
                break

        if text == UPDATE_COMMAND:
            result = "Data is being updated. This may take a moment!"
            data.update_data()

        if result:
            print(result)

        if text.find(END_PHRASE) != -1:  # stop loop
            print("Exit")
            break


main()
