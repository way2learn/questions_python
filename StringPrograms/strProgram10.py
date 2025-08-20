# Python program to accept the strings which contains all vowels
# strProgram10.py
print("Enter the strings saperated by space: ")
vowels_str = [w for w in input().split() if "a" in w and "e" in w and "i" in w and "o" in w oandr "u" in w]
print(f"vowels strs: {vowels_str}")

# # Approach2
print("Enter the strings saperated by space: ")
vowels = set("aeiou")
vowels_str = [w for w in input().split() if vowels.issubset(set(w))]
print(f"vowels {vowels_str}")
