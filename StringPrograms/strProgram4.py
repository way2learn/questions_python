# Ways to remove i’th character from string in Python
# strProgram4.py

# Approach1 Only Works for one occurences of a character, it removes all if we have more W's in the sentence
given_str = "Hi Welcome To Hyderabad and Chennai"
ith_char = given_str[3]
print(ith_char)
split_str_lst = given_str.split(ith_char)
new_str = " ".join(split_str_lst)
print(new_str)

# Approach2
given_str = "Hi Welcome To Hyderabad and Welcome to Chennai"
ith_char = 28
new_str = given_str[0:ith_char] + given_str[29:]
print(new_str)


# Approach3
given_str = "Hi Welcome To Hyderabad and Welcome to Chennai"
ith_char = 28
given_str_lst = list(given_str)
given_str_lst.pop(28)
print(f"{''.join(given_str_lst)}")


# Approach4
given_str = "Hi Welcome To Hyderabad and Welcome to Chennai"
ith_char = 28
new_str = ''.join([val for idx, val in enumerate(given_str) if idx != 28])
print(new_str)
