'''
csv file looks like this:
wa, olypmia
ca, sacramento
id, boise
'''

states = {}

with open("states.csv") as csvFile:
    for line in csvFile:
        items = line.split(',')
        state = items[0].strip()
        capital = items[1].strip()
        states[state] = capital


print(states)
