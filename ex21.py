def add(a,b):
    print(f" Adding {a} + {b}")
    return a + b
    
def subtract (a, b):
    print(f" Subtracting {a} - {b}")
    return a - b

def multiply (a, b):
    print(f" Multiplying {a} * {b}")
    return a * b

def divide (a, b):
    print(f" Dividing {a} / {b}")
    return a / b

print("Let's do some math with just fucntions!")

household = add(2,add(2,6))
savings = subtract(3000, 2000)
bunnies = multiply(4, 4)
serving = divide(24, 6)

print(f"\nThere once was a family of {household}, that had ${savings} they could spend on a pet.\n They choose to purchase bunnies, however they didn't realize that bunnies breed really quickly.\n Soon they had {bunnies} bunnies.\n Concerned about what to do, they had a party with all of their friends and decided to give away {serving} pieces of pizza to each guest.\n They showed everyone the the bunnies and discovered one of their guests was a vet.\n She is going to help limit the bunny population growth.\n\n")

#a puzzle for extra credit
def puzzle(addable, subtractable, multipliable, dividable):

    print("\n\nHere is a puzzle")
    
    print (f" Add: {addable}\n Subtract: {subtractable} \n Multiply: {multipliable} \n Divide: {dividable}\n")
    
    what = add(addable, subtract(subtractable, multiply(multipliable, divide(dividable, 2))))
    
    print("That becomes: ", str(what), "Can you do it by hand?\n")
    
puzzle(household, savings, bunnies, serving)

print("\n\nLet's try again with the values from the example\n")
    
addable = add(30, 5)
subtractable = subtract(78, 4)
multipliable = multiply(90, 2)
dividable = divide(100, 2)    

puzzle(addable, subtractable, multipliable, dividable)