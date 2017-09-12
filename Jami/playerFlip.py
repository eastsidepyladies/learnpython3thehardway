#Given 100 players numbered 1 to 100 and 100 switches turned off intially
# Each player will flip the switch that their number can divide
# For example Player 50 would flip switch 50 and 100.



#let one player flip	
def playerFlip(playerNum, switches):
	index = playerNum - 1
	while index < len(switches):
		switchState = switches[index]
		switches[index] = not (switches[index])
		index += playerNum
	return switches	
		
#find switches that are on
def findPlayer(sequence):
	players = []
	for i in range(len(sequence)):
		if sequence[i]:
			sequence = playerFlip(i+1, sequence)
			players.append(str(i+1))
	return players

#Set up problem			

#Build Binary array
def setSequence(players):
	mySwitches = []
	for i in range(100):
		mySwitches.append(False)
	for player in players:
		mySwitches = playerFlip(player, mySwitches)
	return mySwitches
	
#set up for 2, 3, 5
mySwitches = setSequence ([2,3,5])

#Does it work??

print(findPlayer(mySwitches))

#set up for 100
mySwitches = setSequence ([100])

#Test again

print(findPlayer(mySwitches))



#Does it work for no players??
mySwitches = setSequence ([])
print(findPlayer(mySwitches))

#Does it work for 1 and 100
sequence = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, ]
print(findPlayer(sequence))

#Does it work for 2
sequence = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, ]
sequence = playerFlip(2, sequence)
print(findPlayer(sequence))
