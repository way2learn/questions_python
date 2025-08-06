# Python | Program to print duplicates from a list of integers
# listProgram27.py

# Approach1
lst = [1, 2, 3, 4, 1,2, 3, 4 ,5, 6, 7, 1, 2, 3, 4, 1, 2, 3, 4]
duplicates = []
for elem in lst:
    if lst.count(elem) > 1 and elem not in duplicates:
        duplicates.append(elem)
else:
    print(f"dup: {duplicates}")

# Approach2
lst = [1, 2, 3, 4, 1,2, 3, 4 ,5, 6, 7, 1, 2, 3, 4, 1, 2, 3, 4]
duplicates = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j] and lst[i] not in duplicates:
            duplicates.append(lst[i])
else:
    print(f"duplicates:: {duplicates}")


# Approach3
lst = [1, 2, 3, 4, 1,2, 3, 4 ,5, 6, 7, 1, 2, 3, 4, 1, 2, 3, 4]
unique = set()
duplicates = set()

for elem in lst:
    if elem in unique:
        duplicates.add(elem)
    else:
        unique.add(elem)
else:
    print(f"duplictaes: {list(duplicates)}")
    print(f"unique ements: {list(unique)}")