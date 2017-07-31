# Drill. I'm lost on how to shorten this without just combining lines with ; betwixt
from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file) ; indata = in_file.read()

out_file = open(to_file, 'w') ; out_file.write(indata)

out_file,in_file.close()
