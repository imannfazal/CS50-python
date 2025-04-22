students = ["harry", "hermoine", "ron"]

for i in range(len(students)):
    print(i+1, students[i])

members = {"hermoine": "gryffindor", "draco": "slytherin"}

for member in members:
    print(member, members[member], sep=" belongs to ")

data = [
    {"name":"hermoine", "house": "gryffindor", "patronus": "Otter"},
    {"name":"harry", "house": "gryffindor", "patronus": "stag"},
    {"name":"draco", "house": "slytherin", "patronus": None}
]

for datas in data:
    print(datas["name"], datas["house"], datas["patronus"], sep=", ")