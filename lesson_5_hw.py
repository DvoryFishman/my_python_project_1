import errno
import os
from os import walk
import shutil
from traceback import print_tb
#1
mypath =r"D:\שנה ב\פייתון\lesson 5\create a file_7"
if not os.path.isdir(mypath):
    os.makedirs(mypath)
#2

folders = list(os.walk(mypath))[1:]

for folder in folders:
    # folder example: ('FOLDER/3', [], ['file'])
    if not folder[2]:
        os.rmdir(folder[0])

#3,4
with open(r"D:\שנה ב\פייתון\lesson 5\create a file_7\file_name1.txt", "a") as f:
  f.write("hi!!!!!!")
  print("hello")
  f.close()
#5
os.remove(r"D:\שנה ב\פייתון\lesson 5\create a file_7\file_name2")

#6
file_name = (next(walk(mypath), (None, None, [])))[2]
print(file_name)

#7
print(os.path.abspath(os.getcwd()))

