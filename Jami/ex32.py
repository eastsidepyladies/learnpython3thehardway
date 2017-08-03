the_count = [ 1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'bananana', "kiwi", 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"this is count {number}")

for fruit in fruits:
    print(f"A fruit type: {fruit}")

for i in change:
    print(f"I got {i} back")

elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")
    
