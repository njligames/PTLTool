import json



l = [
"651b029a4a604f6e2e5264e6.json",
"657f547fc08d4352a5913f75.json",
"6589a5a0f05d9e2be074c6cb.json",
"659cb342480dda65f42be361.json",
"65a1c23e415c5782351eec24.json",
"65a54c6b9950d98a42dec398.json",
"65a7099ead1a3a83b54ba572.json",
"65a71ee01e31aa84e29daded.json",
"65b059df5d98a4a8b124a8cc.json"
]

def func(filename):

    f = open(filename)

    data = json.load(f)

    tags = data["tags"]

    for tag in tags:
        # if "cheating" in tag["name"]:
        print(tag)

# for filename in l:
#     print(filename)
#     func(filename)

func("t.json")

