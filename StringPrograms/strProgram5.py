# Python | Check if a Substring is Present in a Given String
# strProgram5.py

# Approach1
given_str = "Welcome to Hyderabd, Bangalore, and Chennai"
sub_str = "Welcomee"
if sub_str in given_str:
    print(f"'{sub_str}' --> is present in given string '{given_str}'")
else:
    print(f"'{sub_str}' --> is not present in given string '{given_str}'")

# Approach2
given_str = "Welcome to Hyderabd, Bangalore, and Chennai"
sub_str = "Welcomer"
if given_str.count(sub_str):
    print(f"'{sub_str}' --> is present in given string '{given_str}'")
else:
    print(f"'{sub_str}' --> is not present in given string '{given_str}'")

# Appraoch3
given_str = "Welcome to Hyderabd, Bangalore, and Chennai"
sub_str = "Welcome"
if len(given_str.split(sub_str)) > 1:
    print(f"'{sub_str}' --> is present in given string '{given_str}'")
else:
    print(f"'{sub_str}' --> is not present in given string '{given_str}'")
