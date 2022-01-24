"""
Healthy Programmer:

The goal of the project is to remind a 9-5 AM working programmer/IT employee to drink 3.5 litre 
water, rest eye after every 30 minutes and do a physical activity after every 45 minutes to stay healthy. 
"""

import time
# import pygame
import datetime
from pygame import mixer  # Load the mixer method from pygame to alarm the programmer
mixer.init()                # initialise the mixer to load the mp3 file


def getdate():
    return datetime.datetime.now()

def action_drink():
    f = open("water.txt", "a+")
    inp = input("Type \"drank\" if you have : ")
    time = ["\n[", str((getdate())), "]"]
    if inp == "drank":
        a = f.writelines(time)
    else:
        print("invalid input")
        action_drink()
    f.close()

def action_eyes():
    f = open("eyes.txt", "a+")
    inp = input("Type \"eydone\" if you have : ")
    time = ["\n[", str((getdate())), "]"]
    if inp == "eydone":
        a = f.writelines(time)
    else:
        print("invalid input")
        action_eyes()
    f.close()

def action_exer():
    f = open("exercise.txt", "w")
    inp = input("Type \"exdone\" if you have : ")
    if inp == "drank":
        a = f.write("datetime.datetime.now()")
    else:
        print("invalid input")
        action_exer()

t = time.time()
print("Welcome to healthy programmer")
for i in range(16):
    time.sleep(30)   
    mixer.music.load('water.mp3')
    mixer.music.play()
    print("Time to drink Water")
    action_drink()
    mixer.music.load('eyes.mp3')
    mixer.music.play()
    print("Time to do Eye exercise")
    action_eyes()

    time.sleep(15)
    mixer.music.load('')
