"I am 5'3\" tall." # here the double quote after 3 needs escaping
'I am 5\'3" tall.' # here the single quote after 5 needs escaping

# \t tabs the tabby in
tabby_cat = "\tI'm tabbed in."
# \n causes line to split
persian_cat  = "I'm spilt\non a line"
# backslash escapes backslash, so that only one prints
backslash_cat = "I'm \\ a \\ cat."

# this  creates a variable for a tabbed list broken up on lines
fat_cat ="""
I''ll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
