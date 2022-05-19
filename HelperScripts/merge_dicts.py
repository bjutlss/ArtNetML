from lib2to3.pygram import python_grammar
import os
import glob
import sys
import json
import yaml

path = sys.argv[1]
count = int(sys.argv[2])
count2 = int(sys.argv[2])
destination = "gt.yml"

python_old_d = {}

with open(path+"scene_gt.json", "r") as f:
    data = json.load(f)
    for key in data:
        value = data[key]
        python_old_d[int(count)] = value
        count+=1

with open(path+"scene_gt_info.json", "r") as f:
    data = json.load(f)
    for key, value in data.items():
        nested = value[0]
        python_old_d[int(count2)][0]["obj_bb"] = nested["bbox_obj"]
        count2 += 1

print(python_old_d)


with open(path+destination, "w") as yamlfile:
    yaml.dump(python_old_d, yamlfile, default_flow_style=None)
