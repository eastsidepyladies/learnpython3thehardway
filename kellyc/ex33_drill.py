def numbers(stop):
    i = 0
    numbers = []

    while i < stop:
        print(f"Hey there {i}")
        numbers.append(i)
        i = i + 1
    print( numbers)

user_limit = int(input("How far should this go?"))
numbers(user_limit)

#  https://stackoverflow.com/questions/21074086/how-to-use-while-loop-inside-a-function
