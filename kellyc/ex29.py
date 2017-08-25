people = 20
cats = 30
dogs = 15

# an if statement is evaluated and if true, processes the print command
if people < cats:
    print("There are too few people. Cats takin' over!")

if people > cats:
    print("There are too many many people. How will the cats take over?!")

if people < dogs:
    print("There are lotsa dogs and too few fire hydrants 'round these parts.")

if people > dogs:
    print("This neighb has too few dogs to pee on fire hydrants. We need to attract more dog owners to settle here.")
# += is shorthand for creating incremental values
dogs += 5

if people >= dogs:
    print("Poople are greater than or equal to dogs.")

if people <= dogs:
    print("Poople are less than or equal to dogs.")

if people == dogs:
    print("Poople are dogs.")
