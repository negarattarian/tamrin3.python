s=input("get a sentence:")
words=s.split()

word_count = len(words)
for word in words:
    if word[-1] in (".", "?", "!"):
        word_count -= 1
print("tedade kalamat:",word_count)


