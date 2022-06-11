from lib2to3.pygram import python_grammar
import os
import glob
import sys
import json
from numpy import empty
import yaml

path = sys.argv[1]
count = int(sys.argv[2])


jpg_files = sorted(glob.glob(path+"*.jpg"))
png_files = sorted(glob.glob(path+"*.png"))
if not png_files:
    png_files = sorted(glob.glob(path+"*.PNG"))

for jpg_file in jpg_files:
    if len(str(count))==1:
        os.rename(jpg_file, path+"00000"+str(count)+".jpg")
        count += 1
    elif len(str(count))==2:
        os.rename(jpg_file, path+"0000"+str(count)+".jpg")
        count += 1
    elif len(str(count))==3:
        os.rename(jpg_file, path+"000"+str(count)+".jpg")
        count += 1
    else:
        os.rename(jpg_file, path+"00"+str(count)+".jpg")
        count += 1


for png_file in png_files:
    if len(str(count))==1:
        os.rename(png_file, path+"000"+str(count)+".png")
        count += 1
    elif len(str(count))==2:
        os.rename(png_file, path+"00"+str(count)+".png")
        count += 1
    elif len(str(count))==3:
        os.rename(png_file, path+"0"+str(count)+".png")
        count += 1
    else:
        os.rename(png_file, path+""+str(count)+".png")
        count += 1
    print("renamed " + str(png_file))
