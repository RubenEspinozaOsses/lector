import json
import os

files = [file for file in os.listdir(os.path.join('files')) if file.endswith('.json')]

for file in files:
    as_json = json.load(open('files/' + file))
    print(as_json[0]['0'].split('\n')[0])

