import sys
import cv2
import numpy as py
import TIS
import time

rpm=input("input rpm: ")
rep=input("input rep: ")


Tis = TIS.TIS()
Tis.selectDevice("5220340",1920,1200, "10/1",TIS.SinkFormats.BGRA,True)
Tis.Start_pipeline()

Tis.List_Properties()
Tis.Set_Property("Gain Auto", False)
Tis.Set_Property("Gain", 0)
Tis.Set_Property("Exposure Auto", False)
Tis.Set_Property("Exposure Time (us)",500)

print("{},{},{},{}".format(Tis.Get_Property("Gain Auto").value,Tis.Get_Property("Gain").value,Tis.Get_Property("Exposure Auto").value,Tis.Get_Property("Exposure Time (us)").value))


