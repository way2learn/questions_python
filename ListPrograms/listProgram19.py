# Python program to print negative numbers in a list
# listProgram19.py

lst = [1, 2, 3, 4, 5, 6, 0, -9, -11, -234, 99, 19]
negatie_nums = []
for elem in lst:
    if elem < 0:
        negatie_nums.append(elem)
else:
    print(f"Negatives elems of a list: {negatie_nums}")