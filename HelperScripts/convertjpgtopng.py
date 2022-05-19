from PIL import Image
import glob
import sys

path = sys.argv[1]
jpg_files = sorted(glob.glob(path+"*.jpg"))

for jpg_file in jpg_files:
    filename = jpg_file.split("/")[-1]
    name = filename.split(".")[0]
    im = Image.open(jpg_file)
    im.save(path+name+'.png')
