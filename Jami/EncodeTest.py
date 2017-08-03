import sys

print(sys.stdout.encoding)

s = "አማርኛ"  # Amharic
raw = s.encode("utf-8", errors="strict")
print(raw)
print(raw.decode("utf-8", errors="strict"))
