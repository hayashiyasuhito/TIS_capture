#coding:utf-8
from serial import Serial
from time import sleep, time
import signal
from pysony import SonyAPI, ControlPoint
import pandas as pd
import re

rpm = input("input rpm: ")
rep = input("input rep: ")
num_camera = input("input camera number: (A)")
exp_min = input("input experiment time: (min)")
exp_time = int(exp_min)*60

serHigh = bytes("h","utf-8")
serLow = bytes("l","utf-8")
#ttyname=input("input ttyname(ttyACM0): ")
#ser = Serial('/dev/{0}'.format(ttyname),9600, timeout=None)

ser = Serial('/dev/ttyACM0',9600, timeout=None)#linux
#ser = Serial("/dev/ttyS5",9600, timeout=None)#win
ser.write(serHigh)

#search = ControlPoint()
#cameras =  search.discover()
#camera = SonyAPI(QX_ADDR=cameras[0])
camera = SonyAPI(QX_ADDR="http://192.168.122.1:8080")
sleep(2)
camera.startRecMode()
sleep(2)
print("camera connected")

l_time=[]
l_filename=[]

start = time()
t=0

if int(rpm) == 47:
  ShootingSpeed = "Hi"
  ShootingTime = 0.7
elif int(rpm) == 22:
  ShootingSpeed = "Mid"
  ShootingTime = 1.4
elif int(rpm) == 15:
  ShootingSpeed = "Mid"
  ShootingTime = 2
elif int(rpm) == 7:
  ShootingSpeed = "Low"
  ShootingTime = 4.3

def mkfilelist(l_time, l_filename):
  df_time=pd.Series(l_time,name="time")
  df_filename=pd.Series(l_filename,name="filename")
  df_filelist=pd.concat([df_time, df_filename],axis=1)
  df_filelist.to_csv("{0}_{1}_{2}.csv".format(num_camera, rpm, rep))

def onoff(arg1,arg2):
  # camera mode single
  camera.setContShootingMode({'contShootingMode': 'Single'})
  # add time to the l_time
  # light on
  ser.write(serLow)
  sleep(0.3)

  # act take picture
  camera.actTakePicture()
  pic_first=camera.awaitTakePicture()
  pic_first_name=re.findall("DSC.*JPG",pic_first["result"][0][0])

  l_time.append(time())
  l_filename.append(pic_first_name[0])
  sleep(2)

  # continuous shooting
  camera.setContShootingMode({'contShootingMode': 'Continuous'})
  sleep(0.1)
  camera.setContShootingSpeed({'contShootingSpeed': ShootingSpeed})
  sleep(0.1)
  camera.startContShooting()
  sleep(ShootingTime)
  camera.stopContShooting()
  sleep(0.1)
  # light off
  ser.write(serHigh)
  mkfilelist(l_time,l_filename)
  t = time()-start
  print(t)

signal.signal(signal.SIGALRM, onoff)
signal.setitimer(signal.ITIMER_REAL,1,240)

while t < exp_time:
  if t > exp_time:
    ser.write(serLow)
    ser.close()
    break

signal.setitimer(signal.ITIMER_REAL,0)

