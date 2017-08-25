def numbers(stop, increment):
    i = 0
    numbers = []

    while i < stop:
        print(f"Hey there {i}")
        numbers.append(i)
        i = i + increment
    print( numbers)

user_limit = int(input("How far should this go?  "))
increment = int(input("What increment should this use?  "))

numbers(user_limit, increment)

#  https://stackoverflow.com/questions/21074086/how-to-use-while-loop-inside-a-function
