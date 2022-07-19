#coding:utf-8
from serial import Serial
from time import sleep, time
import signal
import pandas as pd
import re
import cv2
import subprocess
import sys
import numpy as np
from datetime import datetime
import os

def onoff(arg1,arg2):
    global t
    t = time() - start
    print('time: {}'.format(t))
    cap = cv2.VideoCapture(2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FPS)

    ser.write(serHigh)
    sleep(0.3)

    min_ = datetime.now().strftime("%Y%m%d_%M")
    os.makedirs('./{}/{}_{}/{}'.format(date,rpm,rep,min_),exist_ok=True)
    for i in range(FPS * ShootingTime(rpm)):
        ret, frame = cap.read()
        cv2.imwrite('./{}/{}_{}/{}/{}.jpg'.format(date,rpm,rep,min_,i),frame)

    cap.release()
    ser.write(serLow)

def main():
    signal.signal(signal.SIGALRM, onoff)
    signal.setitimer(signal.ITIMER_REAL,1,60)

    while t < exp_time:
        sleep(1)

def ShootingTime(rpm):
    if int(rpm) == 47:
        ShootingTime=0.7
        FPS = 20
    elif int(rpm) == 22:
        ShootingTime=1
        FPS = 15
    elif int(rpm) == 15:
        ShootingTime=2
        FPS = 10
    elif int(rpm) ==7:
        ShootingTime=3
        FPS = 10
    return ShootingTime, FPS

if __name__ == '__main__':
    ser = Serial('/dev/ttyACM0',9600, timeout=None)#linux
    serHigh = bytes("h","utf-8")
    serLow = bytes("l","utf-8")

    rpm = input('input rpm:7,15,22,47')
    rep = input('input rep:')

    exp_min = input('input experiment time(min): ')
    exp_time = int(exp_min)*60

    ser = Serial('/dev/ttyACM0',9600, timeout=None)#linux

    serHigh = bytes("h","utf-8")
    serLow = bytes("l","utf-8")
    ser.write(serLow)

    WIDTH = 1920
    HEIGHT = 1200
    FPS = 20

    #cp = subprocess.run(["v4l2-ctl","--list-devices"] capture_output=True, text=True)
    subprocess.run(["v4l2-ctl","-d","/dev/video2","-p","{}".format(FPS)])
    subprocess.run(["v4l2-ctl","-d","/dev/video2","-c","brightness=240"])
    subprocess.run(["v4l2-ctl","-d","/dev/video2","-c","gain=0"])
    subprocess.run(["v4l2-ctl","-d","/dev/video2","-v","width={},height={}".format(WIDTH,HEIGHT)])
    subprocess.run(["v4l2-ctl","-d","/dev/video2","-c","exposure_time_absolute=3"])

    start = time()
    t = 0
    main()
