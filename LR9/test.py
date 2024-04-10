import re

text = "Some text, with all\t - possible shit!\n"
#text = "test\t-\ttranslate\n"

words = re.split(r"(\W+)", text)

print(words)

for word in words:
    print(word, end=" ")
print()

