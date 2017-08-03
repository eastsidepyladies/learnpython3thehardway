import sys
script, encoding, error = sys.argv

#To get git Bash to display utf-8 characters type in:
# $ export PYTHONIOENCODING=utf-8

#To test what encoding is being used type in:
# # Gitbash     $ python -c "import sys;print(sys.stdout.encoding)"
# #Powershell >>> chcp


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<=====>", cooked_string)

print("Testing encoding")
#DBES Decode Bytes Encode Strings

# s = "አማርኛ"  # Amharic
# text = s.encode("utf-8", errors="strict")
# print(text)  # This will be fine
# print(text.decode("utf-8", errors="strict"))
# cp437 was used by DOS/Windows. Run "chcp" in your Windows command prompt to know your current code page.
# print(s.encode("cp437", errors="strict"))   This generates the UnicodeEncodeError


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)
