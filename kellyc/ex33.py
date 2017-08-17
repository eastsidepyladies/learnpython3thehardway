i = 0
numbers = []

while i < 6:
    print(f"At the top is {i}")
    numbers.append(i)
    # if you run the above, it will never stop

    i = i + 1
    # Alternately, the above can be written as i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
