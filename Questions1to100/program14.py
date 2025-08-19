# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 
# program14.py

# Approach1
lst = [1, 2, 3, 4, 5, 8, 15, 21, 34, 32, 30, 44, 45, 46, 76, 88]
new_lst = list(filter(lambda x : x % 2 != 0, lst))
print(f"new list: {new_lst}")

# Approach2
lst = [1, 2, 3, 4, 5, 8, 15, 21, 34, 32, 30, 44, 45, 46, 76, 88]
new_lst = [val for val in lst if val % 2 != 0]
print(f"new list: {new_lst}")

# Approach3
lst = [1, 2, 3, 4, 5, 8, 15, 21, 34, 32, 30, 44, 45, 46, 76, 88]
new_lst = []
for val in lst:
    if val % 2 != 0:
        new_lst.append(val)
else:
    print(f"new list: {new_lst}")

