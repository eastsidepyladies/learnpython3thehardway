#from sys import argv
#from os.path import exists

#script, from_file, to_file = argv

#print "Copying from %s to %s" %(from_file, to_file)

#we could do these two on one line too, how?
#in_file = open("test.txt")
#indata = open("test.txt").read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" %exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

out_file = open("new_file.txt", 'w')
out_file.write(open("text.txt").read())

#print "Alright, all done."

out_file.close()
open("text.txt").close()