import sys
import cv2
import numpy as py
import TIS
import time

rpm=input("input rpm: ")
rep=input("input rep: ")

exp_min = input("input experimet time (min):")
exp_time = int(exp_min)*60

Tis = TIS.TIS()
Tis.selectDevice("5220340",1920,1200, "10/1",TIS.SinkFormats.BGRA,True)
Tis.Start_pipeline()

Tis.List_Properties()
Tis.Set_Property("Gain Auto", False)
Tis.Set_Property("Gain", 0)
Tis.Set_Property("Exposure Auto", False)
Tis.Set_Property("Exposure Time (us)",500)

print("{},{},{},{}".format(Tis.Get_Property("Gain Auto").value,Tis.Get_Property("Gain").value,Tis.Get_Property("Exposure Auto").value,Tis.Get_Property("Exposure Time (us)").value))

if int(rpm) == 47:
    ShootingTime=0.7
elif int(rpm) == 22:
    ShootingTime=1
elif int(rpm) == 15:
    ShootingTime=2
elif int(rpm) ==7:
    ShootingTime=3

def mkfilelist(l_time, l_filename):
    df_time=pd.Series(l_time, name="time")
    df_filename=pd.Series(l_filename, name="filename")
    df_filelist=pd.concat([df_time, df_filename], axis=1)
    df_filelist.to_csv("{}_{}_{}.csv".format(num_camera, rpm, rep))

def onoff(arg1, arg2):
    Tis.Set_
