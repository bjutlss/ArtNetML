from PIL import Image as img
import glob
import sys
import numpy as np

path = sys.argv[1]
png_files = sorted(glob.glob(path+"*.png"))

for png in png_files:
    img_data = img.open(str(png), "r")
    img_arr = np.array(img_data)
    print(img_arr)
    img_data.close()
