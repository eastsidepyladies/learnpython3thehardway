print("Mary had a little lamb.")
print("It's fleece was white as {}".format('snow')) # uses positional formatting to insert snow into curly brackets - the "old" way used %d/r/s
print("And everywhere that Mary went.")
print("." * 10) # prints .........

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') # concatenates the "ends" and inserts a space between end6 and end7
print(end7 + end8 + end9 + end10 + end11 + end12)

# this prints
print(end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12)

# this gives the error 'keyword can't be an expression'
# print(end1 + end2 + end3 + end4 + end5 + end6 + end=' ' + end7 + end8 + end9 + end10 + end11 + end12)

# this gives the error 'keyword can't be an expression' - not sure why
# print(end1 + end2 + end3 + end4 + end5 + end6, end=' ', end7 + end8 + end9 + end10 + end11 + end12)

print('come back to')