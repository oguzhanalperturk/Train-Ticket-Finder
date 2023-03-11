from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tkinter import *
from tkinter import messagebox

class catchSeatScreen(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Koltuk Yakalama")

        self.frame1 = Frame(self)
        self.frame1.pack(padx = 5, pady = 5)

        self.SizeLabel = Label(self.frame1, text="Zaman Aralığı: (HH:mm)")
        self.SizeLabel.pack(padx=5, pady=5, side=LEFT)

        self.startTime = Entry(self.frame1, name="start_time")
        self.startTime.pack(padx=5, pady=5, side=LEFT)

        self.SizeLabel = Label(self.frame1, text=" - ")
        self.SizeLabel.pack(padx=5, pady=5, side=LEFT)

        self.endTime = Entry(self.frame1, name="end_time")
        self.endTime.pack(padx=5, pady=5, side=LEFT)

        self.frame2 = Frame(self)
        self.frame2.pack(padx=5, pady=5)

        self.startButton = Button(self.frame2, text ="Başla", command = self.startButtonPressed)
        self.startButton.pack(padx=5, pady=5, side=LEFT)

        self.stopButton = Button(self.frame2, text="Durdur", command=self.stopButtonPressed)
        self.stopButton.pack(padx=5, pady=5)

    def startButtonPressed(self):
        print("start")

    def stopButtonPressed(self):
        print("stop")

if __name__ == "__main__":
    window = catchSeatScreen()
    window.mainloop()