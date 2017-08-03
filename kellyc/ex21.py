def add(a, b):
        # this just prints
        print(f"ADDING {a} + {b}")
        # this is where the math happens (note the value "returned" is calculated but not printed)
        return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

age = add(30,5)
height = subtract(78, 4)
weight = multiply(90,2)
iq = divide(100, 2)

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# what = add(age, subtract(height, multiply(weight, divide(50, 2))))
# what = add(age, subtract(height, multiply(weight, 25)))
# what = add(age, subtract(height, multiply(180, 25)))
# what = add(age, subtract(height, 4500))
# what = add(age, subtract(74, 4500))
# what = add(age, −4426)
# what = add(35, −4426)
# what = add(35, −4426)
# what = −4391


# Drill: 24 + 34 / 100 - 1023

first_part = add (24,43)
second_part = subtract(100,1023)
combined = divide(first_part,second_part)
print(combined)

# the below returns 'TypeError: must be str, not set'
# print(f"Tada ---->" + {combined})
# the below returns 'TypeError: must be str, not float'
# print(f"Tada ---->" + combined)
