name = [
    ['alice', 'bob', 'charlie'], 
    ['david', 'eve', 'frank'], 
    ['grace', 'heidi', 'ivan'], 
    ['judy', 'ken', 'laura'] 
]

for data in nameList:
    if "alice" in data:
        data.remove("alice")
    print(namesList)
else:
name = input("Alice Detected Add New Name:")
namesList.append(name)
print(name)
