# Python | Reversing a List
# listProgram6.py

# Approach1
given_list = [1, 2, 3, 4, 5]
reverse_list = given_list[::-1]
print(reverse_list)

# Approach2
given_list = [1, 2, 3, 4, 5]
given_list.reverse()   # key point we cannot pass this into another variable as it returns None
print(given_list)

# Approach3
given_list = [1, 2, 3, 4, 5]
reverse_list = []
for i in range(len(given_list) - 1, -1, -1):
    reverse_list.append(given_list[i])
else:
    print(f"revered list is : {reverse_list}")
    
# Approach4
given_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(given_list))
print(f"reversed list is: {reversed_list}")

