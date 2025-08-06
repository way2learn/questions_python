# Python – Remove empty List from List

# listProgram23.py

# Approach1
lst = [1, 2, 3, 4 ,5 ,-4, [], [1, 2, 3, 4], (1, 2, 3)]
for elem in lst:
    if elem == []:
        lst.remove([])
else:
    print(f"lst is: {lst}")

# Approach2
lst = [1, 2, 3, 4 ,5 ,-4, [], [1, 2, 3, 4], (1, 2, 3)]
lst.pop(lst.index([]))
print("lst is:",lst)

# Approach3
lst = [1, 2, 3, 4 ,5 ,-4, [], [1, 2, 3, 4], (1, 2, 3)]
for elem in lst:
    if isinstance(elem, list):
        if len(elem) == 0:
            lst.remove(elem)
else:
    print(f"lst is: {lst}")

# Approach4
lst = [1, 2, 3, 4 ,5 ,-4, [], [1, 2, 3, 4], (1, 2, 3)]
lst = [elem for elem in lst if elem != []]
print(f"list is: {lst}")