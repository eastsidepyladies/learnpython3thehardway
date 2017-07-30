from sys import argv
# the exist command checks to see if a file exists, returning True or False
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# in two lines
in_file = open(from_file)
indata = in_file.read()

# in one line - not sure how to do this... 
# in_file = open(from_file,'r').read(indata)

print(f"The input file is {len(indata)} bytes long.")
print("Ready, hit RETURN to continue, ^C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

