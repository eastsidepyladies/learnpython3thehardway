# Branches and Functions

# imports the exit function from sys to allow program to end
from sys import exit

# Definiton of gold room function
def gold_room():
    print("This room is full of gold.  How much do you take?")
    choice = input(">> ")
    # strip removes leading and trailing spaces from input
    choice = choice.strip()
    if all(choice[i] in "0123456789" for i in range(len(choice))):
            # assigns input for "choice" as integer to new variable
            how_much = int(choice)
    else:
        dead("Man, learn how to type a number.")
    if how_much < 50:
        print("You're right. You should only take as much as you can carry.")
        exit()
    else:
            # Not really into calling this sitch "dead" but whatever
            dead("Good luck carrying all of that.")

# Defintion of bear room
def bear_room():
    print("There's a bear in here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # the default is, the bear hasn't moved
    bear_moved = False

    while True:
        choice = input(">> ")

        # the dead option
        if choice == "take honey":
             dead("The bear looks at you and then slaps your face off.")
        # the not-dead option
        elif choice == "taunt bear" and not bear_moved:
            print("The bear moved away from the door.")
            print("You can go through it now.")
            bear_moved = True
        # I don't think the below choice would ever come up?
        # elif choice == "taunt bear" and bear_moved:
        #     dead("The bear gets pissed off and chews your leg off.")
        # elif choice == ("enter room") and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulu_room():
    print("Here you see the great evil Cthulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for you life or eat your head?")

    choice = input(">> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulu_room()


# the string in the above print commands are concateneated with the "good jorb" and then program exits.
def dead(why):
    print(why, "Good jorb!")
    # an exit(0) is a "clean" exit with no errors, while an exit(1) means there were
    exit(0)

# This is the first step in the program flow
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    choice = input(">> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

# This is the main function that starts the program
start()
