# -*- coding:utf-8 -*-
import os
import shutil
name = input("请输入您的用户名")
folderpath = r"C:\\Users\\%s\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"%name
filelist = os.listdir(folderpath)
targetfolde = r"E:\\pic\\"
print(folderpath)
try:
    os.mkdir(targetfolde)
except Exception as e:
    print(e)
print("为您找到",len(filelist),"张图片")
for file in filelist:
    shutil.copy(folderpath+file,targetfolde + file + ".jpg")

