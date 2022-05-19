import os
import glob
import sys
import json
import yaml

path = sys.argv[1]
count = int(sys.argv[2])

png_files = sorted(glob.glob(path+"*.png"))

for png_file in png_files:
        if len(str(count))==1:
            os.rename(png_file, path+"00000"+str(count)+"_label.png")
            count += 1
        elif len(str(count))==2:
            os.rename(png_file, path+"00"+str(count)+"_label.png")
            count += 1
        elif len(str(count))==3:
            os.rename(png_file, path+"0"+str(count)+"_label.png")
            count += 1
        else:
            os.rename(png_file, path+"00"+str(count)+"_label.png")
            count += 1
