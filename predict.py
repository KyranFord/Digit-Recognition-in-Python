import numpy as np
from keras.models import load_model
from keras import models, layers, utils
from tkinter import *
from PIL import ImageGrab
import win32gui
from keras.datasets import mnist
from matplotlib import pyplot as plt


model=load_model('network.h5')

def paint(event):
    color = 'black'
    x1, y1 = (event.x-15), (event.y-15)
    x2, y2 = (event.x+10), (event.y+10)
    c.create_oval(x1,y1,x2,y2,fill=color)

def predict_digit(img):
    img = img.resize((28,28))
    img = img.convert('L')
    img = np.invert(img)
    img = np.array(img)
    img = img.reshape(1,28,28,1)
    img = img/255.0
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

def clearAll():
    c.delete("all")
    outputLabel["text"]=""

def saveImg():
    x=c.winfo_rootx()
    y=c.winfo_rooty()
    canvasinfo = c.winfo_id()
    coords = win32gui.GetWindowRect(canvasinfo)
    grabimg = ImageGrab.grab(coords)
    digit, acc = predict_digit(grabimg)
    outputLabel["text"]= "I think this digit is a " + str(digit)

master = Tk()
master.title("Neural Network Digit Recognition")

c=Canvas(master,width=28*18, height=28*18, bg='white')
c.bind('<B1-Motion>',paint)
b=Button(master, text="Run", command=saveImg)
b2=Button(master, text="Clear", command=clearAll)
c.pack(expand=YES,fill=BOTH,padx=20, pady=20)
outputLabel = Label(master, font=("Arial", 25))
b.pack()
b2.pack()
outputLabel.pack()
master.mainloop()





