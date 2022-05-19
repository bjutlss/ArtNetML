
import sys
import json
import yaml

path = sys.argv[1]
new_path = sys.argv[2]
python_d = {}

with open(path, "r") as f:
    data = json.load(f)
    for key in data:
        value = data[key]
        python_d[key]=value

with open(new_path+".yml", "w") as ymlfile:
    yaml.dump(python_d, ymlfile, default_flow_style=None)