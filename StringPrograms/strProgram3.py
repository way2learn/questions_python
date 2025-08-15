# Reverse words in a given String in Python
# strProgram3.py

# Appraoch1
given_str = input("Enter a string to reverse it's words: ")
words = given_str.split()
reverse_words = []
for word in words:
    reverse_words.append(word[::-1])
else:
    print(f"The reversed words in a given string is: {' '.join(reverse_words)}")
