import sys
#TIS.pyを別フォルダに格納吸う場合は下記のように記載
#sys.path.append("../python-common")

import cv2
import numpy as np
import TIS
import time

# このサンプルはカメラからのイメージ取得とOpenCVで画像処理する一連の処理する方法を記載しています。
# 必要なパッケージ:
# pyhton-opencv
# pyhton-gst-1.0
# tiscamera


Tis = TIS.TIS()
#　DMK 33UX264 Serial: 16710581 、 解像度640x480＠30 fpsで表示する
#　selectDeviceを使ってデバイスをOpenするためコメントアウトしています
#　Tis.openDevice("16710581", 640, 480, "30/1", TIS.SinkFormats.BGRA,True)

#selectDeviceを利用することでデバイスの選択、フォーマット、フレームレートをコマンドラインで指定できる
if not Tis.selectDevice():
        quit(0)



#Gstreamerでの映像伝送
Tis.Start_pipeline() 

#カメラプロパティのリスト一覧を表示(設定範囲を確認)
Tis.List_Properties()


###USB2.0の場合 カメラプロパティ設定
#Tis.List_Properties()で出力されたプロパティ値を引数に渡してください。
# errorが出る場合はコメントアウトしてください。
#Tis.Set_Property("Gain Auto",False)# ゲインを固定化するために自動ゲインをオフにする
#Tis.Set_Property("Gain", 18)
#Tis.Set_Property("Exposure Auto", False)# 露光時間を固定化するために自動露光時間をオフにする
#Tis.Set_Property("Exposure", 11000)
#Tis.Set_Property("whitebalance-auto", False)# ホワイトバランスを固定化するために自動ホワイトバランス調整をオフにする
#Tis.Set_Property("camera-whitebalance", True)# ホワイトバランスを調整するためにTrueにする
#Tis.Set_Property("whitebalance-red", 72)#tcam-captureで調整した値を入力してください。
#Tis.Set_Property("whitebalance-blue", 102)
#Tis.Set_Property("whitebalance-green", 64)

# USB2.0の場合、設定が反映されているか確認
#Tis.List_Properties()で出力されたプロパティ値を引数に渡してください。
# errorが出る場合はコメントアウトしてください。
#print("Gain Auto : %s " % Tis.Get_Property("Gain Auto").value)
#print("Gain : %d" % Tis.Get_Property("Gain").value)
#print("Exposure Auto : %s " % Tis.Get_Property("Exposure Auto").value)
#print("Exposure Time (us) : %d" % Tis.Get_Property("Exposure").value)
#print("Whitebalance Auto : %s " % Tis.Get_Property("whitebalance-auto").value)
#print("Whitebalance Red : %d " % Tis.Get_Property("whitebalance-red").value)
#print("Whitebalance Blue : %d " % Tis.Get_Property("whitebalance-blue").value)
#print("Whitebalance Green : %d " % Tis.Get_Property("whitebalance-green").value)

###USB3.0の場合 カメラプロパティ設定
#Tis.List_Properties()で出力されたプロパティ値を引数に渡してください。
# errorが出る場合はコメントアウトしてください。
#Tis.Set_Property("Gain Auto",False)# ゲインを固定化するために自動ゲインをオフにする
#Tis.Set_Property("Gain", 0)
#Tis.Set_Property("Exposure Auto", False)#露光時間を固定化するために自動露光時間をオフにする
#Tis.Set_Property("Exposure Time (us)", 11000)
#Tis.Set_Property("Whitebalance Auto", False)#ホワイトバランスを固定化するために自動ホワイトバランス調整をオフにする
#Tis.Set_Property("Whitebalance Red", 125)
#Tis.Set_Property("Whitebalance Blue", 124)
#Tis.Set_Property("Whitebalance Green", 123)

# USB3.0の場合、設定が反映されているか確認
#Tis.List_Properties()で出力されたプロパティ値を引数に渡してください。
# errorが出る場合はコメントアウトしてください。
#print("Gain Auto : %s " % Tis.Get_Property("Gain Auto").value)
#print("Gain : %d" % Tis.Get_Property("Gain").value)
#print("Exposure Auto : %s " % Tis.Get_Property("Exposure Auto").value)
#print("Exposure Time (us) : %d" % Tis.Get_Property("Exposure Time (us)").value)
#print("Whitebalance Auto : %s " % Tis.Get_Property("Whitebalance Auto").value)
#print("Whitebalance Red : %d " % Tis.Get_Property("Whitebalance Red").value)
#print("Whitebalance Blue : %d " % Tis.Get_Property("Whitebalance Blue").value)
#print("Whitebalance Green : %d " % Tis.Get_Property("Whitebalance Green").value)


###GigEの場合 カメラプロパティ設定
#Tis.List_Properties()で出力されたプロパティ値を引数に渡してください。
# errorが出る場合はコメントアウトしてください。
#Tis.Set_Property("Gain Auto","Off")# ゲインを固定化するために自動ゲインをオフにする
#Tis.Set_Property("Gain", 30)　
#Tis.Set_Property("Exposure Auto", "Off")# 露光時間を固定化するために自動露光時間をオフにする
#Tis.Set_Property("Exposure", 11000)
#Tis.Set_Property("Whitebalance Auto", "Off")# ホワイトバランスを固定化するために自動ホワイトバランス調整をオフにする
#Tis.Set_Property("Balance Ratio Selector", "Red")
#Tis.Set_Property("Balance Ratio", 2.0)
#Tis.Set_Property("Balance Ratio Selector", "Blue")
#Tis.Set_Property("Balance Ratio", 1.9)
#Tis.Set_Property("Balance Ratio Selector", "Green")
#Tis.Set_Property("Balance Ratio", 1.8)

# GigEの場合、設定が反映されているか確認
#Tis.List_Properties()で出力されたプロパティ値を引数に渡してください。
# errorが出る場合はコメントアウトしてください。
#print("Gain Auto : %s " % Tis.Get_Property("Gain Auto").value)
#print("Gain : %d" % Tis.Get_Property("Gain").value)
#print("Exposure Auto : %s " % Tis.Get_Property("Exposure Auto").value)
#print("Exposure Time (us) : %d" % Tis.Get_Property("Exposure").value)
#print("Whitebalance Auto : %s " % Tis.Get_Property("Whitebalance Auto").value)
#Tis.Set_Property("Balance Ratio Selector", "Red")
#print("Whitebalance Red : " ,Tis.Get_Property("Balance Ratio").value)
#Tis.Set_Property("Balance Ratio Selector", "Blue")
#print("Whitebalance Blue :  " ,Tis.Get_Property("Balance Ratio").value)
#Tis.Set_Property("Balance Ratio Selector", "Green")
#print("Whitebalance Green : " ,Tis.Get_Property("Balance Ratio").value)

print('Press Esc to stop')
lastkey = 0

cv2.namedWindow('Window')  

# OpenCVのerode関数で使う引数
kernel = np.ones((5, 5), np.uint8)  

#カウンター初期化
imagecounter=0

while lastkey != 27:
        #Timeout設定時間（１秒）以内にPCに画像を取得できた場合次の処理へ進む
        if Tis.Snap_image(1) is True:  # Snap an image with one second timeout
                # 画像取得
                image = Tis.Get_image()  
                # OpenCV で画像処理
                image = cv2.erode(image, kernel, iterations=5)  # Example OpenCV image processing

                #画像処理後の画像を表示
                cv2.imshow('Window', image) 
                #Jpegファイルの名称にインデックス番号を付与するためにフレームの数をカウント
                imagecounter += 1
                filename = "./image{:04}.jpg".format(imagecounter)
                #Jpeg画像を保存（コメントアウトしています）
                #cv2.imwrite(filename, image)

        lastkey = cv2.waitKey(10)

# Gstreamerのパイプラインを停止
Tis.Stop_pipeline()
cv2.destroyAllWindows()
print('Program ends')


