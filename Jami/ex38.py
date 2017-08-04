import random

ten_things = "Apples Oranges Crows Telephone Light Sugar Cats Robe Flower Pie"

print("Wait there are not 15 things in that list. Let's fix it.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Spring", "Autumn", "Winter", "Song", "Tea", "Frisbee",
              "Corn", "Cardinal", "Banana", "Girl", "Boy", "Love"]

while len(stuff) != 15:
    next_one = more_stuff.pop(random.randint(0, len(more_stuff) -1))
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("\nLet's do some more things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff[-1])
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
