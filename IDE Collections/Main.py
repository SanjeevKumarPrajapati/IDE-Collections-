from tkinter import *
import tkinter
from PIL import ImageTk, Image
import subprocess
import time
import os
import pyautogui
a=Tk()
a.title("IDE Collection")
a.minsize(1370,750)
a.maxsize(1370,750)
a.iconbitmap("C:\\Users\\acer\\OneDrive\\Pictures\\2.ico")

def dev():
    subprocess.call("C:\Program Files (x86)\Dev-Cpp\devcpp.exe")
    name=int(round(time.time()*1000))
    a.deiconify()
def delay1():
    a.withdraw()
    a.after(1000,dev)
def python():
    subprocess.call("D:\\New folder\\python.exe")
    name=int(round(time.time()*1000))
    a.deiconify()
def python_delay():
    a.withdraw()
    a.after(1000,python)
def vscode():
    subprocess.call("D:\\Visual Studio Code\\Microsoft VS Code\\Code.exe")
    name=int(round(time.time()*1000))
    a.deiconify()
def vs_delay():
    a.withdraw()
    a.after(1000,vscode)
def spyder():
    subprocess.call("spyder.exe")
    name=int(round(time.time()*1000))
    a.deiconify()
def spyder_delay():
    a.withdraw()
    a.after(1000,spyder)
def r():
    subprocess.call("D:\\R studio\\RStudio\\bin\\rstudio.exe")
    name=int(round(time.time()*1000))
    a.deiconify()
def r_delay():
    a.withdraw()
    a.after(1000,r)
def anaconda():
     subprocess.call("jupyter-notebook.exe")
     name=int(round(time.time()*1000))
     a.deiconify()
def ana_delay():
    a.withdraw()
    a.after(1000,anaconda)
image1 = Image.open('img1.jpg').resize((1370,700))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=-2)

lb=Label(a,text="IDE",font=("Arial",50,"bold"),fg="red",bg="skyblue").place(x=480,y=10)
lb=Label(a,text="Collections",font=("Arial",50,"bold"),fg="green",bg="skyblue").place(x=640,y=10)
image1 = Image.open('dev.jpg').resize((400,200))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=20, y=120)
bt1=Button(a,text="Dev C++ IDE",bd=8,bg="skyblue",font=("Arial",14,"bold"),command=delay1).place(x=140,y=330)

image1 = Image.open('python.jpg').resize((400,200))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=480, y=120)
bt1=Button(a,text="Python IDE",bd=8,bg="skyblue",font=("Arial",14,"bold"),command=python_delay).place(x=620,y=330)

image1 = Image.open('spyder.jpg').resize((400,200))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=935, y=120)
bt1=Button(a,text="Spyder IDE",bd=8,bg="skyblue",font=("Arial",14,"bold"),command=spyder_delay).place(x=1080,y=330)

image1 = Image.open('vscode.jpg').resize((400,200))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=20, y=390)
bt1=Button(a,text="VS Code IDE",bd=8,bg="skyblue",font=("Arial",14,"bold"),command=vs_delay).place(x=135,y=600)

image1 = Image.open('RStudio.jpg').resize((400,200))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=480, y=390)
bt1=Button(a,text="R Studio IDE",bd=8,bg="skyblue",font=("Arial",14,"bold"),command=r_delay).place(x=610,y=600)

image1 = Image.open('jupyter.jpg').resize((400,200))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=935, y=390)
bt1=Button(a,text="Jupyter IDE",bd=8,bg="skyblue",font=("Arial",14,"bold"),command=ana_delay).place(x=1080,y=600)
















a.mainloop()
