# 2. Write a Python program to multiply all the items in a list. 
# program2.py

# Approach1
lst = [1, 2, 3, 4, 5]
mul = 1
for elem in lst:
    mul *= elem
else:
    print(f"Multiplication of all elemets of a lst{lst} is: {mul}")


# Approach2
lst = [1, 2, 3, 4, 5]
mul = 1
i = 0
while i < len(lst):
    mul *= lst[i]
    i += 1
else:
    print(f"Mul of a all lst elemsnts {lst} is: {mul}")

