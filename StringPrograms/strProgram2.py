# Python program to check whether the string is Symmetrical or Palindrome
# strProgram2.py

# Approach1
str1 = input("Enter a string to check whether it is palindrome or symmetrical or not: ").lower()
if len(str1) <= 1:
    print("Enter a Valid string")
else:
    if str1 == str1[::-1]:
        print(f"{str1} is a palindrome")
    elif len(str1) % 2 == 0 and str1[:len(str1)//2] == str1[len(str1)//2:]:
        print(f"{str1} is a symmetrical")
    else:
        print(f"Goven {str1} is neither palindrome nor symmetricl")