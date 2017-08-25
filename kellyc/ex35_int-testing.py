choice = input("Type an integer -----> ")
choice = choice.strip()
if len(choice) < 1:
    print("At least take something!")
else:
    if all(choice[i] in "0123456789" for i in range(len(choice))):
        how_much = int(choice)
    elif how_much < 50:
        print("You greedy bastard!")
    else:
        print("Man, learn how to type a number.")
