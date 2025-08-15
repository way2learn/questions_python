# Python program to check if a string is palindrome or not
# strProgram1.py

str1 = input("Enter a string to chek whether it is palindrome or not: ")
if len(str1) <= 1:
    print("Enter a Valid string")
else:
    if str1 == str1[::-1]:
        print(f"given {str1} is palindrome")
    else:
        print(f"{str1} is not a palindrome")