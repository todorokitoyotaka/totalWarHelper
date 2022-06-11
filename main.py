atk = "ATK"
buf = "BUF"
tank = "TANK"
debuf = "DEBUF"

data1 = {"name": "xx1", "tags": ["ATK"]}
data2 = {"name": "xx2", "tags": ["BUF"]}
data3 = {"name": "xx3", "tags": ["TANK", "ATK"]}
data4 = {"name": "xx4", "tags": ["DEBUF"]}
data5 = {"name": "xx5", "tags": ["ATK", "DEBUF"]}
data6 = {"name": "xx6", "tags": ["BUF", "DEBUF"]}
data7 = {"name": "xx7", "tags": ["TANK", "DEBUF"]}

team1 = [data1, data2]
team2 = [data3, data5]

tags = [atk, buf, tank, debuf]
owns = [data1, data4, data6, data7]
needs  = [team1, team2]

print("\n-------- NEEDS ------------")
for team in needs:
    for chara in team:
        if chara["name"] in map(lambda x: x["name"], owns):
            print (chara["name"], end=", ")
            owns = list(filter(lambda x: chara["name"] != x["name"], owns))
        else:
            print (chara["name"]  + "(Lack)", end=", ")
    print("\n--------------------")

for tag in tags:
  count = 0
  print("\n-------- REST "+ tag +" ------------")
  for chara in owns:
    if tag in list(chara["tags"]):
      print(chara["name"], end=", ")
      if count % 5 == 4:
          print(" ")
      count = count + 1

print("\n--------------------")
