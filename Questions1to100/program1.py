# 1. Write a Python program to sum all the items in a list.
# program1.py

# Appraoch1

lst = [1, 2, 3, 4, 5, 6]
sum = 0 # additive opertaor
for item in lst:
    sum = sum + item # sum += item
else:
    print(f"sum is: {sum}")

# Approach2

lst = [1, 2, 3, 4, 5, 6]
sum = 0
i = 0
while i < len(lst):
    sum += lst[i]
    i += 1
else:
    print(sum)