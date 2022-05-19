import os
import glob
import sys
import json
import yaml

path = sys.argv[1]
new_path = sys.argv[2]

if ".json" in path:
    python_d = {}
    python_new = {}

    with open(sys.argv[1], "r") as f:
        data = json.load(f)
        for key in data:
            value = data[key]
            python_d[key]=value

    count = 0
    for key, value in python_d.items():
        python_new[count]= value
        count+=1

    with open(new_path+".json", "w") as jsonfile:
        json.dump(python_new, jsonfile)

    with open(new_path+".yml", "w") as ymlfile:
        yaml.dump(python_new, ymlfile, default_flow_style=None)