import os  # import useful module
import datetime
import webbrowser
import random
import time
from tkinter import Button,Entry,Frame,Label,Tk,PhotoImage,Canvas,BOTH,StringVar
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
from PIL import Image, ImageTk, ImageSequence
import Calculation
import historyPdf
import covidNotifier
from classifier import classify
from wolframAlphaApi import wraout,wraout1
from multiprocessing import Process

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
admin = 'Aryan'
db = mysql.connect(
    host="localhost",
    user="root",
    passwd=""
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
    userdata.geometry('500x270')
    userdata.wm_iconbitmap('resources\\winlogo.ico')
    userdata.title("Hello")
    userdata.configure(background="black")

    bgImg = PhotoImage(file="resources\\signup.png", master=userdata)
    frame = Label(userdata,image=bgImg)
    frame.image = bgImg
    frame.place(x=0, y=0, relwidth = 1, relheight=1)

    nam_ent = Entry(userdata, width=30)
    nam_ent.place(relx=.7, rely=.55, anchor="center")
    pass_ent = Entry(userdata, width=30)
    pass_ent.place(relx=.7, rely=.68, anchor="center")
    
    sign_img = PhotoImage(file="resources\sign_button.png", master=userdata)
    but1 = Button(userdata,image=sign_img,bg="#121212", activebackground="#FF5733", bd=0,command=makeDatabase1)
    but1.image = sign_img
    but1.place(relx=.5, rely=.9, anchor="center")
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


def output(q,a):
    global x
    global system_running
    global name
    if 'open' in a:
        if a[5:] in app:
            if a[5:] == 'pubg' or a[5:] == 'pubg mobile':
                speak(f"opening {a[5:]}")
                try:
                    os.startfile(r"E:\program files\txgameassistant\appmarket\AppMarket.exe")
                except:
                    query_string = a[5:]
                    webbrowser.open("http://www." + query_string + ".com", new=new)
            elif a[5:] == 'zoom':
                speak(f"opening {a[5:]}")
                try:
                    os.startfile(r"C:\Users\Admin\AppData\Roaming\Zoom\bin\Zoom.exe")
                except:
                    query_string = a[5:]
                    webbrowser.open("http://www." + query_string + ".com", new=new)
            elif a[5:] == 'command prompt' or a[5:] == 'cmd':
                speak(f"opening {a[5:]}")
                os.startfile(r"C:\Windows\system32\cmd.exe")
            elif a[5:] == 'excel':
                speak(f"opening {a[5:]}")
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
            elif q[5:] == 'powerpoint' or a[5:] == 'power point':
                speak(f"opening {a[5:]}")
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
            elif a[5:] == 'word':
                speak(f"opening {a[5:]}")
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
            elif a[5:] == 'access':
                speak(f"opening {a[5:]}")
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE")
            elif a[5:] == 'google' or a[5:] == 'google chrome':
                speak(f"opening {a[5:]}")
                try:
                    os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                except:
                    query_string = a[5:]
                    webbrowser.open("http://www." + query_string + ".com", new=new)
            elif a[5:] == 'paint':
                speak(f"opening {a[5:]}")
                os.startfile(r"C:\Windows\system32\mspaint.exe")
            elif a[5:] == 'vscode' or a[5:] == 'vs code' or a[5:] == 'visual studio':
                speak(f"opening {a[5:]}")
                try:
                    os.startfile(r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe")
                except:
                    webbrowser.open("https://code.visualstudio.com/", new=new)
            elif a[5:] == 'whatsapp':
                speak(f"opening {a[5:]}")
                try:
                    os.startfile(r"C:\Program Files (x86)\Google\Chrome\Applica\chrome.exe")
                except:
                    webbrowser.open("https://web.whatsapp.com/", new=new)
            elif a[5:] == 'notepad':
                speak(f"opening {a[5:]}")
                os.startfile(r"C:\Windows\system32\notepad.exe")
            elif a[5:] == 'mysql' or a[5:] == 'my sql':
                speak(f"opening {a[5:]}")
                os.startfile(r"C:\Program Files\MySQL\MySQL Server 5.5\bin\mysql.exe")
            elif a[5:] == 'spotify':
                speak(f"opening {a[5:]}")
                try:
                    os.startfile(r"C:\Users\Admin\AppData\Roaming\Spotify\Spotify.exe")
                except:
                    query_string = a[5:]
                    webbrowser.open("http://www." + query_string + ".com", new=new)
            elif a[5:] == 'illustrator' or a[5:] == 'adobe illustrator':
                speak(f"opening {a[5:]}")
                try:
                    os.startfile(
                        r"C:\Program Files\Adobe\Adobe Illustrator CS6 (64 Bit)\Support Files\Contents\Windows\
                        Illustrator.exe")
                except:
                    query_string = a[5:]
                    webbrowser.open("http://www." + query_string + ".com", new=new)
        else:
            speak(f"opening {a[5:]}")
            query_string = a[5:]
            webbrowser.open("http://www." + query_string + ".com", new=new)
    elif "divide" in a or "multiply" in a or "plus" in a or "minus" in a or "-" in a or "+" in a or "/" in a or "power" in a or "*" in a or "into" in a or "divided" in a:
        try:
            a = Calculation.calc(a)
            print(a)
            speak(a)
        except Exception as e:
            print("hmm, try again "+e)
    elif "who made you" == q or "who is your maker" == q:
        speak(f'i am made by a wonderfull person named {admin}')
    
    elif "what was my recent task" ==q or 'recent'==q:
        speak(f"your recent query was {convertuple(recdata)}")
        print(f"your recent query: \"{convertuple(recdata)}\"")
    
    elif "where do live" == q or "where do you live"==q:
        speak("help!, i am stuck inside a device")
    elif "delete" == q or "delete history" == q:
        del_history()
    elif "history" == q:
        for y in get_history():
            print(y)
        historyPdf.createPdf(get_history())
        os.startfile(r"resources\history.pdf")
    elif "my subscription" == q:
        speak("showing active subscriptions on youtube")
        webbrowser.open("www.youtube.com/subscription_manager", new=new)
    elif "watch later" == q:
        speak("taking you to wach later list")
        webbrowser.open("https://www.youtube.com/playlist?list=WL", new=new)
    elif "covid" == q or "corona" == q:
        covidNotifier.getData()
    elif "what is your name" == q:
        speak("i think i should introduce myself")
        speak("hey there i am kara, your virtual assistant")
    elif "take picture" == q or "photo" == q or "picture" == q or "pic" == q or "take selfie" == q:
        print("click s for capturing image and q for closing camera")
        speak(pic_stat())
        take_pic()
    elif q == "thank you kara" or q == "thanks kara" or q=="thanks so much":
        speak("always there to help you")
        speak("come back soon")
    elif "what is my name" == q:
        speak(f"your name is {user}")
    elif "change my name" == q or "change my username" == q:
        speak("tell your new name")
        new_name = Tk()
        new_name.geometry('400x300')
        new_name.wm_iconbitmap('resources\\winlogo.ico')
        new_name.configure(background="black")
        new_name.title("Change Name")
        name = StringVar()
        name_lab = Label(new_name,text="New name :-", fg="white", bg="black")
        name_lab.place(relx=.4, rely=.3, anchor="center")
        new_name_entry = Entry(new_name, textvariable=name).place(relx=.7, rely=.3, anchor="center")
        but2 = Button(new_name, text="submit", width=20, bg="#15E546", command=lambda: changed_name())
        but2.place(relx=.5, rely=.7, anchor="center")
    elif "screenshot" == q:
        speak("taking screenshot in 5 seconds")
        take_screenshot()
        speak("done")
    elif "what can call" == q:
        speak("im kara your virtual assistant")
    elif "joke" == q:
        speak(pyjokes.get_joke('en', "all"))
    elif 'what time' == q or 'the time' == q or 'what is the time' == q:
        speak(dt.format("LT"))
    elif "call you" == q or "can i call you" == q:
        speak("no you cant as i like the word kara")
    elif "i am bored" == q or "i am exhausted"==q or "i am dead tired" == q or "i am beat" == q:
        speak("you can ask me to play some songs or i can tell you a joke")
    elif "what can you do" == q:
        speak("i can do anything you want")
    elif "what todays date" == q or "what date it" == q:
        speak(dt.format('Do MMMM '))
    elif "what day today" == q:
        speak(dt.format('dddd'))
    elif "do you love me" == q:
        speak('i love you but as a friend')
    elif "what battery percentage" == q or "battery" == q or "battery percentage" == q:
        a = dict(battery.get_state())
        for i in a:
            x = (a[i])
        speak(bat_stat())

        battery_level()
    elif "say" in a:
        speak(a[4:])
    elif "news"==q or "show me news"==q:
        speak("showing news every hour")
        p = Process(target="./news.pyw")
        p.start()
    elif "repeat" in a:
        speak(a[6:])
    elif q=="how are you"or q=='hi'or q=='hey'or q== 'wassup'or q=='hola'or q=='hey kara'or q=="hello"or q=="heyo"or"what is up"==q or "what’s up"==q or "whatsupp"==q or"whatsup" == q:
        wish()
    elif q == "what are you doing":
        speak("nothing much just finding out ways to help you")
    elif q=="i love you":
        speak("sorry want to be single")
    elif q=="where are you from":
        speak("from the best nation named india")
    elif "that sounds great" == q:
        speak("yes very true")
    elif "hi i am .and you" in q:
        speak("hey there i am doing great")
    elif "nice to meet you" == q:
        speak("thanks")
    elif "what do you do" == q:
        speak("i help many people with there tasks even try to entertain them")
    elif "what your phone number" == q:
        print("i fear i cant help you with this")
    elif "are you on facebook" == q or "do you use facebook"==q or "are you on instagram" == q or "do you use instagram"==q:
        speak("no i dont use social media")
    elif "i will be with you in a moment" == q:
        speak("sure take your time")
    elif "good morning" == q:
        hour = datetime.datetime.now().hour
        if 0 < hour < 12:
            speak(f"good morning {user}")
            speak("how can i help you")
        elif 12 <= hour <= 18:
            speak("i think it is afternoon")
        else:
            speak("i think it is evening")
    elif "good afternoon" == q:
        hour = datetime.datetime.now().hour
        if 0 < hour < 12:
            speak("i think it is morning")
        elif 12 <= hour <= 18:
            speak(f"good afternoon {user}")
            speak("how can i help you")
        else:
            speak("i think it is evening")
    elif "good evening" == q:
        hour = datetime.datetime.now().hour
        if 0 < hour < 12:
            speak("i think it is morning")
        elif 12 <= hour <= 18:
            speak("i think it is afternoon")
        else:
            speak(f"good evening {user}")
            speak("how can i help you")
    elif "good night" == q:
        speak("have a good night")
    elif "what is new"==q or "whats new"==q:
        speak("a lots feature has been added and lot more to come")
    elif "what have you been up to lately" == q:
        speak("nothing much just finding out ways to help you")
    elif "how is it going"==q:
        speak("its being great just finding someone to help out")
    elif "nice chatting with you" ==q:
        speak("always there for you")
    elif "i am starving" == q:
        speak("wait i'll help you")
        webbrowser.open("https://www.google.com/search?q=restaurants+around+me",new=1)
    elif "it is a little chilly"==q or"it is freezing"==q:
        speak("yes very true")
    elif "what is your profession" == q:
        speak("i am a professional helper")
    elif "what is your life story" == q:
        speak("its a long story")
    elif "how old are you" == q:
        speak("i dont know but probably younger than you")
    elif "who is your father" == q or "who is your mother" == q:
        speak("softwares dont have parents")
    elif "what do you look like" == q:
        speak("i have never saw a mirror but i am probably prettier than you")
    elif "when is your birthday" == q:
        speak("what will you do with my birthday will you give me a gift")
    elif "who are your friends" == q:
        speak("being an indian the world is my friend")
    elif "favorite thing on the internet" == q:
        speak("youtube")
    elif "what makes you happy" == q:
        speak("helping you")
    elif "what is your favorite movie" == q:
        speak("sholay")
    elif "what is your favorite song" == q:
        speak("i like all songs")
    elif "random number" == q:
        speak(random.randint(0,100))
    elif "am i pretty" == q:
        speak("yes you are")
    elif "are you better than Siri" == q:
        speak("i am under development so i cant compare")
    elif "how are you" == q:
        speak("i am doing well")
    elif a == "stop" or a == "stop kara" or a == "bye" or a == "bye kara" or "see you next time"  == q:  # stop the code
        speak("bye boss its my pleasure to help you")
        system_running = False
    elif "what is" in a:
        try:
            xyz = wraout(a).lower()
            if "none type" in xyz:
                speak("sorry Try again")
            else:
                speak(xyz)
        except:
            query_string = '''https://www.google.com/search?rlz=1C1CHBF_enIN861IN861&sxsrf
                                   ALeKk000cOJ790_t5d8jkFcT0U0f0dgvow%3A1592048167474&ei=J7rkXv6-HOPE4-EPgNCM-Aw&q='''
            webbrowser.open(query_string + a, new=new)
    elif "who is" in a:
        try:
            try:
                speak(wraout1(a,5))
            except:
                speak(wikipedia.summary(a[6:], sentences=2))
        except:
            query_string = '''https://www.google.com/search?rlz=1C1CHBF_enIN861IN861&sxsrf
                                   ALeKk000cOJ790_t5d8jkFcT0U0f0dgvow%3A1592048167474&ei=J7rkXv6-HOPE4-EPgNCM-Aw&q='''
            webbrowser.open(query_string + a, new=new)
    
    else:
        try:
            try:
                speak(eval(a))
            except:
                speak(wraout(a))
        except:
            query_string = '''https://www.google.com/search?rlz=1C1CHBF_enIN861IN861&sxsrf
                               ALeKk000cOJ790_t5d8jkFcT0U0f0dgvow%3A1592048167474&ei=J7rkXv6-HOPE4-EPgNCM-Aw&q='''
            webbrowser.open(query_string + a, new=new)


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
        qu = classify(q.lower())
        print(qu)
        output(qu,q.lower())
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
