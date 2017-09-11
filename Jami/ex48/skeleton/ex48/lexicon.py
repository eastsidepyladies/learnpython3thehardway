lexicon = {
	"north": 'direction',
	"south": 'direction',
	"east": 'direction',
	"west": 'direction',
	"up": 'direction',
	"down": 'direction',
	"left": 'direction',
	"right": 'direction',
	"back": 'direction',
	"go": 'verb',
	"kill": 'verb',
	"stop": 'verb',
	"eat": 'verb',
	"open": 'verb',
	"walk": 'verb',
	"the": 'stop',
	"in": 'stop',
	"of": 'stop',
	"from": 'stop',
	"at": 'stop',
	"it": 'stop',
	"bear": 'noun',
	"princess": 'noun',
	"door": 'noun',
	"cabinet": 'noun',
	
	
}
	
def scan(sentence):
	results = []
	words = sentence.split()
	for word in words:
		if word.isdigit():
			word_type = 'number'
			word = int(word)
		elif word in lexicon:
			word_type = lexicon.get(word)
		else:
			word_type = 'error'
		results.append((word_type, word))
	return results
	

