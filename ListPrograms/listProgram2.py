# Python program to swap two elements in a list
# listProgram2.py

lst = [1, 2, 3, 5]

for i in range(0, len(lst) - 1, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]
else:
    if len(lst) % 2 != 0:
        print(f"List has odd length, So the last element printed as it is {lst[len(lst) - 1]}")
    print(f"Swapped elemts list is: {lst}")
