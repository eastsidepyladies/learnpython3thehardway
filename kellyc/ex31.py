print("""You enter a dark room with two doors.
Do you go through foor #1 or door # 2?""")

door = input(">>>  ")

if door == "1":
    print("There's an average sized bear removing a Sara Lee frozen cake from its package.")
    print("What do you do?")
    print("1. Ask if you can have a slice of cake, after it thaws.")
    print("2. Chastize the bear for having such low dessert standards.")

    bear = input(">>> ")

    if bear == "1":
        print("The bear rolls her eyes and says that waiting for cakes to thaw is for the weak.")
    elif bear == "2":
        print("The bear laughs and wagers a Lemon Chiffon Pie that you wouldn't be able to tell the difference between a freshly thawed Sara Lee cake and a day old freshly baked one.")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear strolls off, trailing crumbs.")

elif door == "2":
    print("You stare into the endless abyss of your mom's retina")
    print("1. electric cigarettes meet shock elevators")
    print("2. pineapple imagery offers solutions")
    print("3. standard buffalos marshall soulfully")

    insanity = input(">>> ")

    if insanity == "1"  or insanity == "2":
        print("Your body survives powered by an endless supply of toothpaste.")
    else:
        print("The insanity causes you to rethink your life and enter a credit counselor correspondence course.")

else:
    print("You stumble around and get lost for a few days. Eventually you hear the moan of an HVAC system and follow it back to civilization.")

# Drill

# Won't work because input is a string :/
# print("Pick a number 1-5")
# num = input("---> ")
# if 1 >= num <= 4:
#     print("You're good at this game.")
# else:
#     print("Erghgngnh.")
