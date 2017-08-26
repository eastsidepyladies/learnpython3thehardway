# Designing and Debugging

from sys import exit

# Define kale situation
def kale_sitch():
    print()
    print("There's only one bunch of kale left and someone else grabs it! What do you do?")
    print()
    print("Here are your options: ")
    print()
    print("a: Say something about the weather and take some baby spinach instead.")
    print("b: You remember this is a game and take the kale from them forcefully.")
    print("c: Decide you want the red-leaf lettuce after all.")
    sitch_over = False

    while True:
        print()
        print("Which option will it be? a, b, or c?")
        choice1 = input(">> ")

        if choice1 == "a":
            womp_womp("You take the least wilted bunch of spinach you can find.")
        elif choice1 == "b" and not sitch_over:
            print("It's uncharacteristic of you, but you wrench the kale away from them with no real harm done. Easy!")
            freezer_aisle()
        else:
            womp_womp("You take the least wilted bunch of red-leaf lettuce you can find.")

# Define freezer aisle sitch
def freezer_aisle():
    print()
    print("You've got a craving for a Klondike bar, so you head to the frozen section.")
    print()
    print("In the way is an Abominable Snowman. What do you do?")
    print()
    print("a: Laugh at it and say 'I'm not real, this is just your dream.'")
    print("b: Ask it whether it whether you should go with the crunchy chocolate shelled Klondike bars or stick with the original.")
    print("c: Tackle the Snowman and tie it up.")
    print()
    print("Which option will it be? a, b, or c?")
    print()
    sitch_over = False

    while True:
        choice2 = input(">> ")

        if choice2 == "a":
            womp_womp("The snowman doesn't laugh and only looks at you pityingly. You realize that what you've said is in fact true; you are merely a figment of that great creature's imagination. You remind yourself that you still have a role to play. ")
        elif choice2 == "b":
            womp_womp("The Snowman thinks for a moment and then suggests original before pushing his cart towards the frozen lemonade concentrate. ")
        elif choice2 == "c":
            print("The Snowman goes down fairly easy, but this is probably because you've been working out. You take the dream journal in your bag out and make a line through an item on your bucket list.")
            lost_list()
        else:
            womp_womp("The Snowman knocks you around a bit but you are able to get away and finish your shopping. ")

# Define lost list area
def lost_list():
    print()
    print("What a weird day you are having! There was something else on your list, but now you can't find it. It was just in your hand... ")
    print()
    print("What do you do?")
    print()
    print("a: Drop your basket where you are and leave. You're lost without a list.  ")
    print("b: Resign yourself to the fact that you just have to buy one of everything in the store, so you go back to the front to exchange your basket for a cart. ")
    print("c: Dump your bag out on the floor and dig around until you find it. ")
    print()
    sitch_over = False

    while True:
        choice3 = input(">> ")

        if choice3 == "a":
            print("Just as you are heading out, you spot your list spiked on top of a pineapple. You return to your basket and continue shopping.")
            anything_else()
        elif choice3 == "b":
           womp_womp("As you start to take one of everything of the shelf, you realize how ridiculous this mission is but do not stop. You decide you'll donate what's left over after you stock your kitchen. Shopping takes all day but eventually you finish.  ")
        elif choice3 == "c":
            print("This trick always works. You locate the list as well as a couple other things that have gone missing in the past week. ")
            anything_else()
        else:
           womp_womp("You find the rest of the stuff on your list without incident. ")

# Define anything else
def anything_else():
    print()
    print("What else is on your list?")
    print()
    print("Is it ground beef, detergent, or cereal?")
    sitch_over = False

    while True:
        choice4 = input(">> ")

        if choice4 == "ground beef":
            womp_womp("You head to the meat counter, narrowly escaping being crushed under a collapsing shelf. The rest of your shopping goes without incident. ")
        elif choice4 == "detergent":
            womp_womp("You head to the cleaning products aisle, narrowly escaping being crushed under a collapsing shelf. The rest of your shopping goes without incident. ")
        elif choice4 == "cereal":
            womp_womp("When you get to the cereal aisle, you are astonished to find all of the characters on the box have come to life. They turn out to be very nice and they find you to be very pleasant, as humans go. A lunch date is made and everyone goes about their business. ")
        else:
            womp_womp("That item... may not be sold here? You ask an attendant and they confirm this. Well, at least you got most of the stuff on your list.")

# Define the start
def start():
    print("You've decided you need to do some grocery shopping, so you head to the store.")
    print("Did you remember to bring your reusable grocery bags?")
    global reusable_bags
    reusable_bags =  input(">> ")

    print("You head to the produce deptartment because you want to make a salad. What sort of greens do you want, kale or red-leaf lettuce?")
    sitch_over = False

    while True:
        greens = input(">> ")

        if greens == "kale":
            kale_sitch()
        elif greens  == "red-leaf lettuce":
            womp_womp("You pick out a nice, fresh-looking bunch. ")
        else:
            print("Fine, you don't have to play.")
            exit(0)

def womp_womp(why):
    if reusable_bags == "yes":
        print(why, "You head to the cashier and checkout. Eventfully, you're handed a coupon for your favorite yogurt with the receipt. ")
        exit(0)
    else:
        print(why, "You feel a little guilty about forgetting your reusable bags.")
        exit(0)

start()
