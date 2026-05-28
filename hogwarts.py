students = [
    {"name": "jeff", "house": "gryffindor", "patronous": "otter"},
    {"name": "harry", "house": "gryffindor", "patronous": "stag"},
    {"name": "dranco", "house": "gryffindor", "patronous": "JRT"},
    {"name": "ron", "house": "slytherin", "patronous": None },    
]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep = ",")