#create a mapping of stat to abbreviation
states = {
    'Oregon': 'OR',
    'Washington': 'WA',
    'California': 'CA',
    'Florida': 'FL',
    'New York': 'NY',
    'Michigan' : 'MI',
    'Kentucky': 'KY',
    'Ohio': 'OH',
    'Indiana': 'IN',
    'Texas': 'TX',
    'Kansas': 'KS'

}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Orlando',
    'IN': 'Bloomington',
    'KY': 'Louisville',
    'WA': 'Redmond',
    'TX': 'Austin'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['OH'] = 'Columbus'
cities['KS'] = 'Wichita'

# print out some cities
print('-' * 15)
print("NY State has: ", cities['NY'])
print("WA State has: ", cities['WA'])
print("OR State has: ", cities['OR'])
print("IN State has: ", cities['IN'])
print("KS State has: ", cities['KS'])
print("\n")

#print some states
print('-' * 15)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
print("Kentucky's abbreviation is: ", states['Kentucky'])
print("Texas's abbreviation is: ", states['Texas'])
print("\n")

#do it by using the state then city dict
print('-' * 15)
print ( "California has: " , cities [ states [ 'California' ]])
print ( "Ohio has: " , cities [ states [ 'Ohio' ]])
print("\n")

#print every state abbreviation
print('-' * 15)
for state , abbrev in list ( states . items ()):
    print ( f"{state} is abbreviated {abbrev}" )
print("\n")

#print every city in state
print('-' * 15)
for abbrev , city in list ( cities . items ()):
    print ( f"{abbrev} has the city {city}" )
print("\n")

#now do both at the same time
print('-' * 15)
for state , abbrev in list ( states . items ()):
    print ( f"{state} state is abbreviated {abbrev}", end = ' ' )
    print ( f"and has city {cities[abbrev]}" )
print("\n")

#safely get an abbreviation by state that might not be there
print('-' * 15)
state = states.get('Maine')

if not state:
    print("sorry, no Maine.")

#get a city with a default value
city = cities.get('GA', 'Does Not Exist')
print(f"The city for the state 'GA' is: {city}")
