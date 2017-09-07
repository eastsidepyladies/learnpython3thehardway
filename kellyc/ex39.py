# Dictionaries, Oh Lovely Dictionaries

# Create a mapping of state to abbreviation
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
    }

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print mo citiies
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbeviation is ", states['Michigan'])
print("Florida's abbreviation is ", states['Florida'])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{abbrev} is abbreviated {abbrev}.")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}.")

# do both - at the same time!
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# here's a safe way to try and retrieve an abbreviation that may not exist
state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")

# now have it deliver a default value when city doesn't exist
city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}.")
