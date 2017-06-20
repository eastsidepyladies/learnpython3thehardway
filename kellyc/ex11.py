# What the end=' '  is doing here is telling print to not end the line with a \n and to add a space
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

# Below wouldn't print so I tried to concatenate string differently
# print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print("So, you're " + age + " old, " +  height + " tall, and " + weight + " heavy.")

print("come back to")
