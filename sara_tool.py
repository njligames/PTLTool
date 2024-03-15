import json

f = open('data.json')

data = json.load(f)

tags = data["tags"]

for tag in tags:
    if "cheating" in tag["name"]:
        print(tag)

