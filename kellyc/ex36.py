from sys import exit

# Define kale situation
def kale_sitch():
    print("There's only one bunch of kale left and someone else grabs it! What do you do?")
    print("Here are your options: ")
    print("a : Say something about the weather and take some baby spinach instead.")
    print("b: You remember this is a game and take the kale from them forcefully.")
    print("c : Decide you want the red-leaf lettuce after all.")
    sitch_over = False

    while True:
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
    print("You've got a craving for a Klondike bar, so you head to the frozen section.")
    print("In the way is an Abominable Snowman. What do you do?")
    print("a : Laugh at it and say 'I'm not real, this is just your dream.'")
    print("b: Ask it whether it whether you should go with the crunchy chocolate shelled Klondike bars or stick with the original.")
    print("c : Tackle the Snowman and tie it up.")
    print("Which option will it be? a, b, or c?")
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
    print("What a weird day you are having! There was something else on your list, but now you can't find it. It was just in your hand... ")
    print("What do you do?")
    print("a: Drop your basket where you are and leave. You're lost without a list.  ")
    print("b: Resign yourself to the fact that you just have to buy one of everything in the store, so you go back to the front to exchange your basket for a cart. ")
    print("c : Dump your bag out on the floor and dig around until you find it. ")
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
    print("What else is on your list?")
    print("Is it ground beef, detergent, or cereal?")
    sitch_over = False

    while True:
        choice4 = input(">> ")

        if choice4 == "ground beef":
            womp_womp("You head to the meat counter, narrowly escaping being crushed under a collapsing shelf. The rest of your shopping goes with incident. ")
        elif choice4 == "detergent":
            womp_womp("You head to the cleaning products aisle, narrowly escaping being crushed under a collapsing shelf. The rest of your shopping goes with incident. ")
        elif choice4 == "cereal":
            checkout("When you get to the cereal aisle, you are astonished to find all of the characters on the box have come to life. They turn out to be very nice and they find you to be very pleasant, as humans go. A lunch date is made and everyone goes about their business. ")
        else:
            womp_womp("That item... may not be sold here? You ask an attendant and they confirm this. Well, at least you got most of the stuff on your list.")

# Define checkout
def checkout(why):
    print(why, "This has been a more fun day than expected. Maybe tomorrow I'll go to the hardware store. You head to the checkout. ")
    if reusable_bags == "yes":
        womp_womp("Yep, that's a good idea.")
    elif reusable_bags == "no":
        womp_womp("There's no one else in line! You feel a little guilty about forgetting your reusable bags.")


# Define the start
def start():
    print("You've decided you need to do some grocery shopping, so you head to the store.")
    print("Did you remember to bring your reusable grocery bags?")

    reusable_bags =  input(">> ")

    print("You head to the produce deptartment because you want to make a salad. What sort of greens do you want, kale or red-leaf lettuce?")
    sitch_over = False

    while True:
        choice4 = input(">> ")
        greens = input(">> ")

        if greens == "kale":
            kale_sitch()
        elif greens  == "red-leaf lettuce":
            womp_womp("You pick out a nice, fresh-looking bunch. ")
        else:
            print("Fine, you don't have to play.")
            exit(0)

def womp_womp(why):
    print(why, "You head to the cashier and checkout. Eventfully, you're handed a coupon for your favorite yogurt with the receipt. ")
    exit(0)

start()

# A visit to the supermarket

# You decide to do some grocery shopping so head to the store. Did you remember to bring your reusable grocery bags? (If no, tell the customer they are a monster at end-of-game/checkout)

# You head to the produce department to get ingredients for a salad. What sort of greens do you get, kale or red-leaf lettuce? (If kale, say that just as they are about to grab the last bunch, a hipster snags it. What do you do? a) say something snarky and grab baby spinach instead. b) remember that this is just a game, punch the hipster out and take the kale c) compliment the hipster on their taste in pocketwatches and grab the red-leaf lettuce instead. If red-leaf, nothing eventful happens.

# You've got a craving for a Klondike bar, so you head to the frozen section. In the way is an Abominable Snowman. What do you do? a) Laugh at it and say "I'm not real, this is just your dream." b) Ask it whether it whether you should go with the crunchy chocolate shelled Klondike bars or stick with the original. (It replies, go with the original. Classic!) c) Tackle the bear and tie it up. (Afterwards, you take your dream journal out of your bag and make a line through an item on your bucket list.)

# What a weird day you are having! There was something else on your list, but now you can't find it. It was just in your hand! Do you a) drop your basket where you are and leave. You're lost without a list. b) resign yourself to the fact that you just have to buy one of everything in the store, so you go back to the front to exchange your basket for a cart c)  d) Dump your bag out on the floor and dig around until you find it.

# What else do you need? Cereal, dishwashing detergent, or ground beef?

# If ground beef, encounter scene where you have to decide how lean.
# If cereal, encounter aisle full of cereal box characters come to life.
# if dishwashing detergent, have difficulty finding it and get lost in store trying to find an attendant (worse outcome of whole game is hidden in this option.)

# You make your way to the front. All the items you've acquired are in your cart, aka an array. The array is checked for the characters you encountered, who may have snuck into your basket/car (shrunken, of course). If found, the cashier calls the manager over. The manager then checks and if they are the cereal characters or the snowman, says "No problem here!" and then "good riddance" under his breath as he walks away. If it's the hipster, the manager says, "You just had to have the kale, huh? You should let him go. He is a person too." You can let him go and continue checking out, or refuse and run.

# The cashier gives you a random amount (formatted as USD) to pay and you a) pay in pennies or b) pay with a card.

# To be continued...
