# Dictionaries, Oh Lovely Dictionaries

# Create a mapping of state to abbreviation
states = {
        'Oregon' :  'OR',
        'Florida' :  'FL',
        'California' :  'CA',
        'New York' :  'NY',
        'Michigan' :  'MI'
        }

# create a basic set of states and some cities in them
cities = {
    'CA' :  'San Francisco',
    'MI' :  'Detroit',
    'FL' :  'Jacksonville'
    }

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print mo citiies
print('-' * 10)
print("NY State has :  ", cities['NY'])
print("OR State has :  ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbeviation is ", states['Michigan'])
print("Florida's abbreviation is ", states['Florida'])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()) :
    print(f"{state} is abbreviated {abbrev}.")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()) :
    print(f"{abbrev} has the city {city}.")

# do both - at the same time!
print('-' * 10)
for state, abbrev in list(states.items()) :
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# here's a safe way to try and retrieve an abbreviation that may not exist
state = states.get('Texas')
if not state :
    print("Sorry, no Texas.")

# now have it deliver a default value when city doesn't exist
city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is :  {city}.")


# Drills

items1 = {
        'lemon' : 'produce',
        'cod' : 'fresh meat and fish',
        'laundry detergent' : 'cleaning supplies',
        'aspirin' : 'health',
        'yogurt' : 'dairy',
        'green apple' : 'produce'
}

quantities = {
        'lemon' : 3,
        'cod' : 2,
        'laundry detergent' : 1,
        'aspirin' : 1,
        'yogurt' : 5,
        'green apple' : 8
}

items1['lemonade concentrate'] = 'freezer'
items1['red pepper flakes'] = 'spice'
items1['capers'] = 'canned goods'

print('~*~' * 10)
print("You can find lemons in the", items1['lemon'], "department.")
print("You can find cod in the", items1['cod'], "department.")

print('~*~' * 10)
print("I need to buy", quantities['green apple'], "green apples.")
print("I need to buy", quantities['cod'], "pieces of cod.")

print('~*~' * 10)
for item, dept in list(items1.items()):
    print(f"You can find {item} from the {dept} department.")

print('~*~' * 10)
for item, quant in list(quantities.items()):
    print(f"I need to buy {quant} unit(s) of {item}.")
