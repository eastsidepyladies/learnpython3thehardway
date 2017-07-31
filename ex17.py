from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
indata = open(from_file).read()


print(f"the input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")

print("Ready, hit Return to begin, CTRL + C to abort.")

input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()

""""
#first make a sample filee
echo "This is a test file." > test.txt
# then look at it to make sure it created correctly
cat test.txt

#now run script
python3.6 ex17.py test.txt new_file.txt
"""