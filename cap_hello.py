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

def initial_setup():
    global exp_time
    exp_time = 20
    global start
    start = time()

def onoff(arg1,arg2):
    global t
    t = time() - start
    print('time: {}'.format(t))

def main():
    signal.signal(signal.SIGALRM, onoff)
    signal.setitimer(signal.ITIMER_REAL,1,5)

    while t < exp_time:
        sleep(1)

if __name__ == '__main__':
    initial_setup()
    t = 0
    main()
