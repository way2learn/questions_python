# Find length of a string in python (4 ways)
# strProgram8.py

given_str = input("Enter a string to find it's length: ")
if len(given_str) == 0:
    print("You must enter the string")
else:
    print("Using length function")
    print("*"*25)
    print(f"Length of a string '{given_str}' is: {len(given_str)}")
    print("Using for for loop")
    print("*"*25)
    str_len = 0
    for char in given_str:
        str_len += 1
    else:
        print(f"Length of a string '{given_str}' is: {str_len}")
    print("Using while loop")
    print("*"*25)
    strw_len = 0
    try:
        while given_str[strw_len]:
            strw_len += 1
    except IndexError as ie:
        print(f"Length of a string '{given_str}' is: {strw_len}")
    print("Using enumerate")
    print("*"*25)
    count = 0
    for idx, char in enumerate(given_str):
        count = idx + 1
    else:
        print(f"Length of a string '{given_str}' is: {count}")
    print("Using count function")
    print("*"*25)
    print(f"Length of a string '{given_str}' is: {given_str.count("") - 1}")
    print("Using reduce special function")
    print("*"*25)
    import functools
    l = functools.reduce(lambda x, _ : x + 1, given_str, 0)
    print(l)