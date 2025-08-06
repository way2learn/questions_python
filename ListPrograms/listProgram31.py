# Python | Sort the values of first list using second list
# listProgram31.py

# Approach1
lst1 = ['apple', 'banana', 'cherry']
lst2 = [3, 1, 2]
sorted_lst = []
for _, y in sorted(zip(lst2, lst1)):
    sorted_lst.append(y)
else:
    print(f"sorted list: {sorted_lst}")

