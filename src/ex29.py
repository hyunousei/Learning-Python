people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!") # This one will be printed

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!") # This one will be printed

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.") # This one will be printed

if people <= dogs:
    print("People are less than or equal to dogs.") # This one will be printed

if people == dogs:
    print("People are dogs.")