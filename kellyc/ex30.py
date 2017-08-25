people = 20
cars = 30
trucks = 30

if cars > people:
    print("We should take the cars.")
# elif creates another condition to check for truthiness
elif cars < people:
    print("We should not take the cars.")
# if truthiness is not met in above, the else is the "what else" that happens
else:
    print("We can't decide.")

if trucks > cars:
    print("Thats' too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# Drills

if cars > people:
    print("These people are outnumbered by cars.")
elif trucks > people:
    print("These people are outnumbered by trucks.")
else:
    print("A win for mankind! Not enough automobiles showed up.")

if people == cars and people == trucks:
    print("We can finally plan that Triples Night at the demo derby we discussed. Yes!")
else:
    print("Maybe that was not such a good idea. Or... have you given much thought to motorcycles?")
