# Python program to print positive numbers in a list
# listProgram18.py
lst = [1, 2, 3, 4, 5, 6, 0, -9, -11, -234, 99, 19]
positive_nums = []
for elem in lst:
    if elem >= 0:
        positive_nums.append(elem)
else:
    print(f"Positives elems of a list: {positive_nums}")
