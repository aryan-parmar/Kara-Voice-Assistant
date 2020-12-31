import os
from tkinter import *
import sys


def install_process():
    start_button.destroy()
    lod_tex = Label(install, text="installing modules in background...", bg="black", fg="white",
                    font=("Megrim", 20, "bold"))
    lod_tex.place(rely=.5, relx=.5, anchor="center")
    install.after(4010, install_process2)
    install.after(4010, lambda: install.destroy())

def install_process2():
    a = sys.version
    if '64 bit' in a:
        if "3.9.0" in a:
            os.system('cmd /c "pip install pyaudio\PyAudio-0.2.11-cp39-cp39-win_amd64.whl"')
            os.system('cmd /C "pip install speechRecognition"')
            os.system('cmd /C "pip install -r requirements.txt"')
            os.system('cmd /C "python UI.py"')
        else:
            os.system('cmd /c "pip install pyaudio\PyAudio-0.2.11-cp38-cp38-win_amd64.whl"')
            os.system('cmd /C "pip install speechRecognition"')
            os.system('cmd /C "pip install -r requirement.txt"')
            os.system('cmd /C "python UI.py"')
    else:
        if "3.9.0" in a:
            os.system('cmd /c "pip install pyaudio\PyAudio-0.2.11-cp39-cp39-win32.whl"')
            os.system('cmd /C "pip install speechRecognition"')
            os.system('cmd /C "pip install -r requirement.txt"')
            os.system('cmd /C "python UI.py"')
        else:
            os.system('cmd /c "pip install pyaudio\PyAudio-0.2.11-cp38-cp38-win32.whl"')
            os.system('cmd /C "pip install speechRecognition"')
            os.system('cmd /C "pip install -r requirement.txt"')
            os.system('cmd /C "python UI.py"')


try:
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
    os.system('cmd /c "python UI.py')
except:
    install = Tk()
    install.geometry("500x200")
    install.title("Installing modules")
    install.configure(bg="black")
    install.wm_iconbitmap(r'resources/winlogo.ico')
    start_button = Button(install, bg="#15E546", text="start installing...", command=install_process)
    start_button.place(rely=.5, relx=.5, anchor="center")
    install.mainloop()
