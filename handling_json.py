import json

exclude_list = [
    "[Music]",
    "[Applause]",
    "[Laughter]",
    # etc...
]

with open("fauna.json",  "r") as json_file :
    data = json.load(json_file)

for ele in data :

    toprint = ele["text"]
    if toprint not in exclude_list :
        print(ele["text"])