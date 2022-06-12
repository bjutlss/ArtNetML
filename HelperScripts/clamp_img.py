from PIL import Image as img
import glob
import os
import sys
import numpy as np

path = sys.argv[1]
png_files = sorted(glob.glob(path+"*.png"))
<<<<<<< HEAD
new_path = path
print(png_files)
=======
new_path = path+"multiplied/"

>>>>>>> f5ca5e185fea8b589c42efac2b3e93361219d72f
for png in png_files:
    img_data = img.open(str(png), "r")
    img_arr = np.array(img_data)
    img_data.close()
    multiply_arr = np.full((1920, 1440), 0.01, dtype=np.float32)
    multiplied_arr = np.multiply(img_arr, multiply_arr)
    new_arr = multiplied_arr.astype(dtype=np.int32)
    filename = png.split("/")[-1]
    new_img = img.fromarray(new_arr)
    new_img.save(str(new_path)+str(filename))
<<<<<<< HEAD
    print("Saved "+filename+" as clamped png")
=======
>>>>>>> f5ca5e185fea8b589c42efac2b3e93361219d72f
