# import modules 
import os
import pyttsx3
from tkinter import *
from englisttohindi.englisttohindi import EngtoHindi 
from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound

engine = pyttsx3.init('sapi5')
#engine = pyttsx3.init()
#engine.setProperty("language",'hi')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak():
    gTTS(text = res, lang = lang).write_to_fp(voice := NamedTemporaryFile())
    playsound(voice.name)
    voice.close()


def speak1():
    engine.say(str(e.get()))
    engine.runAndWait()

# user define funtion 
def eng_to_hindi(): 
	trans = EngtoHindi(str(e.get())) 
	global res
	res = trans.convert
	result.set(res) 


# object of tkinter 
# and background set for grey 
master = Tk() 
master.configure(bg = 'light grey') 

# Variable Classes in tkinter 
result = StringVar(); 
lang='hi'

# Creating label for each information 
# name using widget Label 
Label(master, text="Enter Text : " , bg = "light grey").grid(row = 0, sticky = W) 
Label(master, text="Result :", bg = "light grey").grid(row = 3, sticky = W) 

# Creating lebel for class variable 
# name using widget Entry 
Label(master, text="", textvariable=result,bg = "light grey").grid(row = 3, 
																column = 1, 
																sticky = W) 

e = Entry(master, width = 100) 
e.grid(row = 0, column = 1) 

# creating a button using the widget 
# Button that will call the submit function 
b = Button(master, text = "Show", command = eng_to_hindi, bg = "Blue") 
b.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5,) 
b = Button(master, text = "Speak_in",command = speak1, bg = "green") 
b.grid(row = 2, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5,) 
b = Button(master, text = "Speak_ou",command = speak, bg = "green") 
b.grid(row = 4, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5,) 

master.mainloop()
