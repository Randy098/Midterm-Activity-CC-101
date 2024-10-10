name = [
    ['alice', 'bob', 'charlie'], 
    ['david', 'eve', 'frank'], 
    ['grace', 'heidi', 'ivan'], 
    ['judy', 'ken', 'laura'] 
]

for hello in name:
    for names in hello:
        print(names)

name[0].remove("alice")

new_name = input("Alice Detected Add New Name:")
name[0].append(new_name)
print(name)