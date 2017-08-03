i = 3
value = 0
numbers = [2]

def is_valid(value):
    try:
        value = int(upper)
        return value >= 3
    except ValueError:
        print("Please enter a number")
        return False

upper = input("How high do you want to search for prime numbers? ")

while not is_valid(upper):

    print("Please select a value higher than 2")
    upper = input("Highest number to search for prime numbers: ")

upper =  int(upper)
while i < upper:

    #print(f"At the top i is {i}")
    add = True
    for num in numbers:
        if i % num == 0:
            add = False
            break

    if add:
        numbers.append (i)
        print("Numbers now: ", numbers)

    i += 2
    #print(f"At the bottom i is {i}")


print("The prime numbers")

for num in numbers:
    print(num)
