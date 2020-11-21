from logic import *

class SplashScreen:
    def __init__(self, parent):
        self.parent = parent
        self.gambar = Image.open(r'resources/log2.gif')
        imagew, imageh = self.gambar.size
        setscreenw = (self.parent.winfo_screenwidth() - imagew) // 2
        setscreenh = (self.parent.winfo_screenheight() - imageh) // 2
        self.parent.geometry("%ix%i+%i+%i" % (imagew, imageh, setscreenw, setscreenh))
        self.parent.configure(background="black")
        self.canvas = Canvas(self.parent,cnf={"width":imagew, "height":imageh})
        self.canvas.pack(fill=BOTH)
        self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('resources\\log2.gif'))]
        self.image = self.canvas.create_image(400,300,image=self.sequence[0])
        self.parent.after(4050, lambda: self.parent.destroy())
        self.animate(2)

        #self.splashWindow()

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))

class mainroot:
    def __init__(self):
        self.sroot = Tk()
        self.sroot.geometry('1280x800')
        self.sroot.wm_iconbitmap(r'resources/winlogo.ico')
        self.sroot.minsize(1280, 760)
        self.sroot.maxsize(1280, 760)
        self.sroot.configure(background="black")
        self.sroot.title("KARA")

        bgImg = PhotoImage(file="resources\\bg.png", master=self.sroot)
        frame = Label(self.sroot,image=bgImg)
        frame.image = bgImg
        frame.place(x=0, y=0, relwidth = 1, relheight=1)

        mic1 = PhotoImage(file="resources\\micr.png", master=self.sroot)
        self.mic = Button(self.sroot, image=mic1, command=self.startMic, bg="white", activebackground="#FF5733",bd=0)
        self.mic.place(relx=.5, rely=.6, anchor="center")
        self.mic.image = mic1

        his_img = PhotoImage(file="resources\history.png", master=self.sroot)
        self.his = Button(self.sroot, image=his_img, command=lambda: output("history"),bg="white", activebackground="#FF5733", bd=0)
        self.his.image = his_img
        self.his.place(relx=.9, rely=.05, anchor="center")
        

        his_del_img = PhotoImage(file="resources\del.png", master=self.sroot)
        self.his_del = Button(self.sroot, image=his_del_img, command=lambda: del_history(),bg="white", activebackground="#FF5733", bd=0)
        self.his_del.place(relx=.97, rely=.05, anchor="center")
        self.his_del.image = his_del_img

        self.covid_button = Button(self.sroot, text="get info about corona cases in india, and take precautions", bg="black", fg="white",
                                   activebackground="#FF5733", borderwidth=1, highlightthickness=0, padx=9, height=1,
                                   font=("arial", 10),
                                   command=lambda : webbrowser.open("https://www.covid19india.org/"))
        self.covid_button.place(relx=.5, rely=0.95, anchor="center")
        
        name = username()
        self.name_lab = Label(self.sroot,text=name, font=("open serif", 60, "bold"), bg="white", bd=0)
        self.name_lab.place(relx=.6, rely=0.29, anchor="center")

        hide_lab = Label(self.sroot, bg="white", height=10, width=50)
        hide_lab.place(relx=.3, rely=0.75, anchor="center")

    def startMic(self):
        input()


if __name__ == '__main__':
    root = Tk()
    root.overrideredirect(True)
    app = SplashScreen(root)
    root.after(4010, mainroot)
    root.mainloop()
