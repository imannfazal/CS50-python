students = ["harry", "hermoine", "ron"]

for i in range(len(students)):
    print(i+1, students[i])

members = {"hermoine": "gryffindor", "draco": "slytherin"}

for member in members:
    print(member, members[member], sep=" belongs to ")