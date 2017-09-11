lexicon = {
	"north": 'direction',
	"south": 'direction',
	"east": 'direction',
	"west": 'direction',
	"go": 'verb',
	"kill": 'verb',
	"eat": 'verb',
}
	
def scan(sentence):
	results = []
	words = sentence.split()
	for word in words:
		word_type = lexicon.get(word)
		results.append((word_type, word))
	return results
