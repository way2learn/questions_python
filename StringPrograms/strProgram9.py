# Python program to print even length words in a string
# strProgram9.py
str1 = "Welcome to Mumbai to eat wada pav, it is very good in taste"
words = str1.split()
even_length_words = [w for w in words if len(w) % 2 == 0]
print(even_length_words)