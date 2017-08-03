print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")
while door != "1" and door != "2":
    print("You must select a door")
    print("Do you go through door 1 or door 2?")
    door = input("> ")


if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Offer to pour some tea for the bear.")


    bear = input("> ")
    # while bear != "1" and bear != "2" and bear != "3":
    #     print("You must select how to interact with the bear.")
    #     print("Select 1 to Take the cake, 2 to Scream, or 3 to Offer tea")
    #     bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")

    elif bear =="2":
        print("The bear eats your legs off. Good job!")

    elif bear =="3":
        print("You have a lovely time and the bear becomes your new loyal protector")

    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powerd by a mind of jello")
        print("Good job!")

    else:
        print("The insanity rots your eyse into a pool of muck.")
        print("Good job!")
