# Python program to find largest number in a list
# listProgram10.py

# Approach1
lst = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
print(f"largest({lst}) = {max(lst)}")

# Approach2
lst = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 10]
largest = lst[0]
for i in range(1, len(lst)):
    if lst[i] > largest:
        largest = lst[i]
else:
    print(f"Largest Number of a list {lst} is: {largest}")