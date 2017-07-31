def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
    
print("We can just give the fucntion numbers directly:")
cheese_and_crackers(10,30)

print("OR, we can use variables in our script:")
amount_of_cheese = 20
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers( 10 + 20, 5 ** 3)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese * 14, amount_of_crackers * 24)
    