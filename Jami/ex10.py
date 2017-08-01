tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnit\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


escape_sequence = """
\\ \\\\ Backslash\n 
\' \\' Single-quote(')\n 
\" \\" Double quotes\n 
\a \\a ASCII bell (BEL)\n 
\b \\b ASCII backspace (BS)\n 
\f \\f ASCII formfeed (FF)\n 
\n \\n ASCII linefeed (LF) ie new line\n 
\N{Black Chess Knight} \\N{name} Character named name in the Unicode database (Unicode only)\n 
\r \\r Carrage return (CR)\n 
\t \\t Horizontal tab (Tab)\n 
\u2764 \\uxxxx Character with 16-bit hex value xxxx\n 
\U0001da1d \\Uxxxxxxxx Character with 32-bit hex value xxxxxxxx\n 
\v \\v ASCII vertical tab (VT)\n 
\123 \\ooo Character with octal value ooo\n 
\4A \\xhh Character with the hex value hh\n 
"""

print(escape_sequence)