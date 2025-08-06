# Python program to find smallest number in a list
# listProgram9.py

# Approach1
lst = [66, 2, 3 ,4, 5, -1, 0]
print(f"{min(lst)} is the smallest")

# Approach2
lst = [66, 2, 3 ,4, 5, -1, 0]
small = lst[0]
for i in range(1, len(lst)):
    if lst[i] < small:
        small = lst[i]
else:
    print(f"{small} is the smalllest in the list")

# Approach3
lst = [66, 2, 3 ,4, 5, -1, 0]
lst.sort()
print(lst[0])

# Approach4
lst = [66, 2, 3 ,4, 5, -1, 0]
print(sorted(lst)[0])