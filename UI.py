from logic import *


class SplashScreen:
    def __init__(self, parent):
        self.gambar = Image.open(r'resources/logo.png')
        self.gambar = self.gambar.resize((920, 550), Image.ANTIALIAS)
        self.parent = parent
        self.imgSplash = ImageTk.PhotoImage(self.gambar)
        self.splashWindow()

    def splashWindow(self):
        imagew, imageh = self.gambar.size
        setscreenw = (self.parent.winfo_screenwidth() - imagew) // 2
        setscreenh = (self.parent.winfo_screenheight() - imageh) // 2
        self.parent.geometry("%ix%i+%i+%i" % (imagew, imageh, setscreenw, setscreenh))
        self.logo = Label(self.parent, image=self.imgSplash)
        self.logo.pack()
        self.parent.after(4050, lambda: self.parent.destroy())


class mainroot:
    def __init__(self):
        wish()
        self.sroot = Tk()
        self.sroot.geometry('1920x1080')
        self.sroot.wm_state("zoomed")
        self.sroot.wm_iconbitmap(r'resources/winlogo.ico')
        self.sroot.minsize(1080, 890)
        self.sroot.configure(background="black")
        self.sroot.title("KARA")

        self.label = Label(self.sroot, text="Kara", bg="black", fg="white", font=("Megrim", 150, "bold"))
        self.label.place(relx=.5, rely=.5, anchor="center")

        mic = Image.open(r"resources/mic.png")
        mic1 = ImageTk.PhotoImage(mic, master=self.sroot)
        self.mic = Button(self.sroot, text="", image=mic1, command=self.startMic, compound=TOP, bg="black",
                          activebackground="#FF5733", borderwidth=0, highlightthickness=0, padx=10, pady=10)
        self.mic.place(relx=.5, rely=.7, anchor="center")

        self.his = Button(self.sroot, text="HISTORY", command=lambda: output("history"), bg="black", fg="white",
                          activebackground="#FF5733", borderwidth=1, highlightthickness=0, padx=10, pady=10,
                          font=("arial", 20, "bold"))
        self.his.place(relx=.5, rely=.8, anchor="center")
        self.covid_button = Button(self.sroot, text="get info about corona cases in india, and take precautions", bg="black", fg="white",
                                   activebackground="#FF5733", borderwidth=1, highlightthickness=0, padx=9, height=1,
                                   font=("arial", 10),
                                   command=lambda : webbrowser.open("https://www.covid19india.org/"))
        self.covid_button.place(relx=.5, rely=0.95, anchor="center")
        bgImg = Image.open(r"resources/grad.png")
        bgImg = bgImg.resize((int(self.sroot.winfo_screenwidth() + 1), int((self.sroot.winfo_screenheight() / 3) + 2)),
                             Image.ANTIALIAS)
        bgImg1 = ImageTk.PhotoImage(bgImg, master=self.sroot)
        canvas = Canvas(self.sroot, width=self.sroot.winfo_screenwidth(), height=(self.sroot.winfo_screenheight() / 3),
                        borderwidth=0, highlightthickness=0, bg="black")

        canvas.create_image(0, 0, image=bgImg1, anchor="nw")
        canvas.pack(expand=False, fill="both")
        frame = Frame(canvas, width=self.sroot.winfo_screenwidth(), height=(self.sroot.winfo_screenheight() / 3))
        frame.place(x=0, y=0, anchor="center", index=0)

    def startMic(self):
        input()


if __name__ == '__main__':
    root = Tk()
    root.overrideredirect(True)
    app = SplashScreen(root)
    root.after(4010, mainroot)
    root.mainloop()
