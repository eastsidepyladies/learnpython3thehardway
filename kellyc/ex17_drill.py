# Drill. I'm there are ways to shorten this more, but am not sure how other than to combine all rows using ;
from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file) ; indata = in_file.read()

out_file = open(to_file, 'w') ; out_file.write(indata)

out_file,in_file.close()


