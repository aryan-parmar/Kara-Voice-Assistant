import os  # import useful module
import datetime
import webbrowser
import random
import time
from tkinter import *
from tkinter.ttk import Progressbar
from plyer import battery
import pendulum
import pyautogui
import cv2
import pyjokes
import mysql.connector as mysql
from PIL import Image, ImageTk
import wikipedia
import pyttsx3 as p
import speech_recognition as sr

import Calculation
import historyPdf
import covidNotifier

engine = p.init('sapi5')  # initiating speak engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 2.0)
new = 2
app = ("zoom", "google", "google chrome", "spotify", "powerpoint", "power point", "paint",
       "whatsapp", 'vscode', 'vs code', 'visual studio', "command prompt", 'cmd', "mysql", "my sql", 'excel', 'access',
       'illustrator', 'word', 'instagram')
i = 1

# defining part starts from here

dt = pendulum.now('Asia/Calcutta')
a = random.randint(1, 2)
admin = 'Kalios'
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="1234"
)
data = db.cursor()

try:
    data.execute("USE karadb")
except:
    data.execute("CREATE DATABASE karadb")
    db.commit()


def makeDatabase1():
    pas = pass_ent.get()
    nam = nam_ent.get()
    data.execute("CREATE TABLE karadb(id INT(5), name VARCHAR(20), password VARCHAR(20), recent VARCHAR(50))")
    data.execute("INSERT INTO karadb(id, name, password) VALUES(1, %s, %s)", (nam, pas))
    db.commit()
    userdata.destroy()


try:
    data.execute("USE karadb")
    data.execute("SELECT id FROM karadb")
    no_use_data = data.fetchall()
except:
    data.execute("USE karadb")
    userdata = Tk()
    userdata.geometry('500x200')
    userdata.wm_iconbitmap('resources\\winlogo.ico')
    userdata.title("Hello")
    userdata.configure(background="black")

    nam = Label(userdata, text="Name :-", bg="black", fg="white")
    pas_lab = Label(userdata, text="Password :-", bg="black", fg="white")
    nam.place(relx=.3, rely=.3, anchor="center")
    pas_lab.place(relx=.3, rely=.4, anchor="center")

    nam_ent = Entry(userdata, width=30)
    nam_ent.place(relx=.7, rely=.3, anchor="center")
    pass_ent = Entry(userdata, width=30)
    pass_ent.place(relx=.7, rely=.4, anchor="center")
    but1 = Button(userdata, text="Enter", width=20, bg="#15E546", command=makeDatabase1)
    but1.place(relx=.5, rely=.6, anchor="center")
    userdata.mainloop()

try:
    data.execute("USE karadb")
    data.execute("SELECT user FROM recent_data")
    no_use_data = data.fetchall()
except:
    data.execute("USE karadb")
    data.execute("CREATE TABLE recent_data(time VARCHAR(50),user VARCHAR(20), query VARCHAR(50), date VARCHAR(50))")
    db.commit()


def convertuple(tup):
    stri = ''.join(tup)
    return stri


def username():
    data.execute("USE karadb")
    data.execute("SELECT name FROM karadb")
    databases = data.fetchall()
    us = databases[0]
    usern = convertuple(us)
    return usern


user = username()


def change_name(nm):
    data.execute("USE karadb")
    query = "UPDATE karadb SET name =\'" + nm + "\'WHERE id = '1'"
    data.execute(query)
    db.commit()


def recent(strre):
    data.execute("USE karadb")
    query = "UPDATE karadb SET recent =\'" + strre + "\'WHERE id = '1'"
    data.execute(query)
    db.commit()


def getrecent():
    data.execute("USE karadb")
    data.execute("SELECT recent FROM karadb")
    databases = data.fetchall()
    dataa = databases[0]
    rec = dataa
    return rec


def getpasswrd():
    data.execute("USE karadb")
    data.execute("SELECT password FROM karadb")
    databases = data.fetchall()
    ps = databases[0]
    passn = ps
    return passn


def history(user, recent):
    data.execute("USE karadb")
    data.execute(
        "INSERT INTO recent_data VALUES ('" + dt.format("LT") + "','" + user + "','" + recent + "','" + dt.format(
            "LL") + "')")
    db.commit()


def get_history():
    data.execute("use karadb")
    data.execute("SELECT* from recent_data")
    datarec = data.fetchall()
    return datarec


def del_history():
    data.execute("use karadb")
    data.execute("DELETE FROM recent_data")
    db.commit()


def speak(audio):  # speaks the output
    engine.say(audio)
    engine.runAndWait()


def battery_level():
    c = dict(battery.get_state())
    m = c["isCharging"]
    y = c["percentage"]
    if m != 'charging':
        if 1 < y < 20:
            speak("battery is low connect charger")
        else:
            speak("battery is sufficient")


def wish():  # just wishes u
    hour = datetime.datetime.now().hour
    if 0 < hour < 12:
        speak(f"good morning {user}")
        speak("how can i help you")
    elif 12 <= hour <= 18:
        speak(f"good afternoon {user}")
        speak("how can i help you")
    else:
        speak(f"good evening {user}")
        speak("how can i help you")


def bat_stat():
    if a == 1:
        y = f"{x} percentage of battery is left"
    else:
        y = f"percentage of battery is {x}"
    return y


def pic_stat():
    if a == 1:
        w = "say cheese"
    else:
        w = "smile please"
    return w


def take_pic(image_counter=0):
    face_cascade = cv2.CascadeClassifier(
        r'resources\haarcascade_frontalface_alt.xml')
    video = cv2.VideoCapture(0)
    video.set(3, 852)
    video.set(4, 480)
    while True:
        check, frame = video.read()
        gray_f = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        gray_flip = cv2.flip(frame, 1)
        cv2.imshow("kara", gray_flip)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break
        elif key == ord('s'):
            # SPACE pressed
            img_name = "kara_capture{}.png".format(image_counter)
            cv2.imwrite(img_name, gray_f)
            print("{} captured!".format(img_name))
            image_counter += 1
    video.release()
    cv2.destroyAllWindows()


# welcoming the user


def take_screenshot(ss=1):
    time.sleep(5)
    pyautogui.screenshot().save(f"screenshot{ss}.jpg")


# welcoming the user


def changed_name():
    a = name.get()
    change_name(a)
    speak("done")
    username()
    print("username will change when you restart the program")


def output(q):
    global x
    global system_running
    global name
    if 'open' in q:
        if q[5:] in app:
            if q[5:] == 'pubg' or q[5:] == 'pubg mobile':
                speak(f"opening {q[5:]}")
                try:
                    os.startfile(r"E:\program files\txgameassistant\appmarket\AppMarket.exe")
                except:
                    query_string = q[5:]
                    webbrowser.open("http://www." + query_string + ".com", new=new)
            elif q[5:] == 'zoom':
                speak(f"opening {q[5:]}")
                try:
                    os.startfile(r"C:\Users\Admin\AppData\Roaming\Zoom\bin\Zoom.exe")
                except:
                    query_string = q[5:]
                    webbrowser.open("http://www." + query_string + ".com", new=new)
            elif q[5:] == 'command prompt' or q[5:] == 'cmd':
                speak(f"opening {q[5:]}")
                os.startfile(r"C:\Windows\system32\cmd.exe")
            elif q[5:] == 'excel':
                speak(f"opening {q[5:]}")
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
            elif q[5:] == 'powerpoint' or q[5:] == 'power point':
                speak(f"opening {q[5:]}")
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
            elif q[5:] == 'word':
                speak(f"opening {q[5:]}")
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
            elif q[5:] == 'access':
                speak(f"opening {q[5:]}")
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE")
            elif q[5:] == 'google' or q[5:] == 'google chrome':
                speak(f"opening {q[5:]}")
                try:
                    os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                except:
                    query_string = q[5:]
                    webbrowser.open("http://www." + query_string + ".com", new=new)
            elif q[5:] == 'paint':
                speak(f"opening {q[5:]}")
                os.startfile(r"C:\Windows\system32\mspaint.exe")
            elif q[5:] == 'vscode' or q[5:] == 'vs code' or q[5:] == 'visual studio':
                speak(f"opening {q[5:]}")
                try:
                    os.startfile(r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe")
                except:
                    webbrowser.open("https://code.visualstudio.com/", new=new)
            elif q[5:] == 'whatsapp':
                speak(f"opening {q[5:]}")
                try:
                    os.startfile(r"C:\Program Files (x86)\Google\Chrome\Applica\chrome.exe")
                except:
                    webbrowser.open("https://web.whatsapp.com/", new=new)
            elif q[5:] == 'notepad':
                speak(f"opening {q[5:]}")
                os.startfile(r"C:\Windows\system32\notepad.exe")
            elif q[5:] == 'mysql' or q[5:] == 'my sql':
                speak(f"opening {q[5:]}")
                os.startfile(r"C:\Program Files\MySQL\MySQL Server 5.5\bin\mysql.exe")
            elif q[5:] == 'spotify':
                speak(f"opening {q[5:]}")
                try:
                    os.startfile(r"C:\Users\Admin\AppData\Roaming\Spotify\Spotify.exe")
                except:
                    query_string = q[5:]
                    webbrowser.open("http://www." + query_string + ".com", new=new)
            elif q[5:] == 'illustrator' or q[5:] == 'adobe illustrator':
                speak(f"opening {q[5:]}")
                try:
                    os.startfile(
                        r"C:\Program Files\Adobe\Adobe Illustrator CS6 (64 Bit)\Support Files\Contents\Windows\
                        Illustrator.exe")
                except:
                    query_string = q[5:]
                    webbrowser.open("http://www." + query_string + ".com", new=new)
        else:
            speak(f"opening {q[5:]}")
            query_string = q[5:]
            webbrowser.open("http://www." + query_string + ".com", new=new)
    elif "who made you" in q or "who is your maker" in q:
        speak(f'i am made by a wonderfull person named {admin}')
    elif "what was my recent task" in q or 'recent' in q:
        speak(f"your recent query was {convertuple(recdata)}")
        print(f"your recent query: \"{convertuple(recdata)}\"")
    elif "where do you live" in q:
        speak("help!, i am stuck inside a device")
    elif "you" in q and "look" in q:
        print("(^_^)")
    elif "delete" in q or "delete history" in q:
        del_history()
    elif "history" in q:
        for y in get_history():
            print(y)
        historyPdf.createPdf(get_history())
        os.startfile(r"history.pdf")
    elif "my subscriptions" in q or "my subscription" in q:
        speak("showing active subscriptions on youtube")
        webbrowser.open("www.youtube.com/subscription_manager", new=new)
    elif "watchlater" in q or "watch later" in q:
        speak("taking you to wach later list")
        webbrowser.open("https://www.youtube.com/playlist?list=WL", new=new)
    elif "covid" in q or "corona" in q:
        covidNotifier.getData()
    elif "what is your name" in q or "whats your name" in q or "your name" in q:
        speak("i think i should introduce myself")
        speak("hey there i am kara, your virtual assistant")
    elif "take picture" in q or "photo" in q or "picture" in q or "pic" in q or "take selfie" in q:
        print("click s for capturing image and q for closing camera")
        speak(pic_stat())
        take_pic()
    elif q == "thank you kara" or q == "thanks" or q == "thank you" or q == "thanks kara":
        speak("always there to help you")
        speak("come back soon")
    elif "what is my name" in q:
        speak(f"your name is {user}")
    elif "change my name" in q or "change my username" in q or 'change' in q:
        speak("tell your new name")
        new_name = Tk()
        new_name.geometry('400x300')
        new_name.wm_iconbitmap('resources\\winlogo.ico')
        new_name.configure(background="black")
        new_name.title("Change Name")
        name = StringVar()
        name_lab = Label(text="New name :-", fg="white", bg="black")
        name_lab.place(relx=.4, rely=.3, anchor="center")
        new_name_entry = Entry(new_name, textvariable=name).place(relx=.7, rely=.3, anchor="center")
        but2 = Button(new_name, text="submit", width=20, bg="#15E546", command=lambda: changed_name())
        but2.place(relx=.5, rely=.7, anchor="center")
    elif "take" in q or "screenshot" in q:
        speak("taking screenshot in 5 seconds")
        take_screenshot()
        speak("done")
    elif "what can i call" in q:
        speak("im kara your virtual assistant")
    elif "joke" in q:
        speak(pyjokes.get_joke('en', "all"))
    elif 'what time' in q or 'the time' in q or 'what\'s the time' in q:
        speak(dt.format("LT"))
    elif "can" in q and "i" in q and "call you" in q:
        speak("you can but i love my original name given by my maker")
    elif (("i" in q and "am" in q) or "im" in q) and ("bored" in q or "bore" in q):
        speak("you can ask me to play some songs or i can tell you a joke")
    elif "what can you do" in q:
        speak("i can do anything you want")
    elif "what is todays date" in q or "what is todays date" in q or "what date it is" in q:
        speak(dt.format('Do MMMM '))
    elif "what day it is today" in q or ("day" in q and "today" in q):
        speak(dt.format('dddd'))
    elif "do you love me" in q or "love" in q:
        speak('i love you but as a friend')
    elif "what is battery percentage" in q or "battery" in q or "left" in q or "battery percenntage" in q:
        a = dict(battery.get_state())
        for i in a:
            x = (a[i])
        speak(bat_stat())

        battery_level()
    elif "what is" in q:
        try:
            speak(wikipedia.summary(q[8:], sentences=2))
        except:
            query_string = '''https://www.google.com/search?rlz=1C1CHBF_enIN861IN861&sxsrf
                                   ALeKk000cOJ790_t5d8jkFcT0U0f0dgvow%3A1592048167474&ei=J7rkXv6-HOPE4-EPgNCM-Aw&q='''
            webbrowser.open(query_string + q, new=new)
    elif "who is" in q:
        try:
            speak(wikipedia.summary(q[6:], sentences=2))
        except:
            query_string = '''https://www.google.com/search?rlz=1C1CHBF_enIN861IN861&sxsrf
                                   ALeKk000cOJ790_t5d8jkFcT0U0f0dgvow%3A1592048167474&ei=J7rkXv6-HOPE4-EPgNCM-Aw&q='''
            webbrowser.open(query_string + q, new=new)
    elif "say" in q:
        speak(q[4:])
    elif "repeat" in q:
        speak(q[6:])
    elif "hey" in q or "hi" in q or "hello" in q:
        wish()
    elif "how are you" in q:
        speak("i am doing well")
    elif q == "stop" or q == "stop kara" or q == "bye" or q == "bye kara":  # stop the code
        speak("bye boss its my pleasure to help you")
        system_running = False
    elif "divide" in q or "multiply" in q or "plus" in q or "minus" in q or "-" in q or "+" in q or "/" in q or "power" in q or "*" in q or "into" in q or "divided" in q:
        try:
            a = Calculation.calc(q)
            print(a)
            speak(a)
        except:
            print("hmm, try again")
    else:
        try:
            speak(eval(q))
        except:
            query_string = '''https://www.google.com/search?rlz=1C1CHBF_enIN861IN861&sxsrf
                               ALeKk000cOJ790_t5d8jkFcT0U0f0dgvow%3A1592048167474&ei=J7rkXv6-HOPE4-EPgNCM-Aw&q='''
            webbrowser.open(query_string + q, new=new)


recdata = getrecent()
mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()


def input():
    required = 0
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "pulse" in name:
            required = index
    r = sr.Recognizer()
    with sr.Microphone(device_index=required) as source:
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = 4000
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=5)
    try:
        q = r.recognize_google(audio, show_all=False, language="en-IN")
        print(q)
        output(q.lower())
        try:
            if q != "history" or q != "delete":
                history(username(), q)
                recent(q)
            else:
                pass
        except:
            pass
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("seem's like you are offline")
