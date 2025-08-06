# Python | Sum of number digits in List
# listProgram29.py

# Approach1
lst = [1, 2, 3, 4, 5,6, 7, 8, "ALPHA"]
sum = 0
for elem in lst:
    if type(elem) == int:
        sum = sum + elem
else:
    print(f"sum is: {sum}")

# Approach2 
lst = [1, 2, 3, 4, 5,6, 7, 8, "ALPHA"]
sum = 0
for elem in lst:
    if isinstance(elem, int):
        sum += elem
else:
    print(f"sum: {sum}")