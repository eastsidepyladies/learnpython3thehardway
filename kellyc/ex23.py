import sys
script, input_encoding, error = sys.argv

# calling this function main is a programming convention that makes functions easier to read/understand
def main(language_file, encoding, errors):
    # reads one line from language_file and returns empty string when it reaches end of file
    line = language_file.readline()

    # this iterates through language_file, printing all the read lines until the end
    if line:
        print_line(line, encoding, errors)
        # main is being called inside main to create a loop (the if statement ensures it won't run forever)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    #  this strips the trailing \n on each line
    next_lang = line.strip()
    #  this encodes the human readable values in text file
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # this decodes (makes human readable) the encoded value from above
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("ex23_languages.txt", encoding="utf-8")

# This is what actually runs the main function and specifys the correct parameterss
main(languages, input_encoding, error)

# Run this like so  >> python ex23.py utf-8 strict

# Notes
# DBES => decode bytes, encode strings
# According to conventions taught by this book, bytes are sequences of 8 bits with binary values (1s and 0s)
# Additional conventions exist whereby bytes are encoded using a different number of bits
# ASCII is limited in ability to represent characters beyond what's typically found in the English speaking world
# Solution: Unicode
# Unicode characters use 32 bits for a total of 4,294,967,295 possibilities
# 32 and even 16 are a bit wasteful if you mostly need characters able to be encoded in 8 bits so decompression encoding was introduced to extend the range only when necessary to represent characters outside of what 8-bits can represent
