# Remove multiple elements from a list in Python
# listProgram22.py

# Approach1
lst = [10, 20, 30, 40, 50, 60]
to_remove = [20, 40, 60]
print(list(set(lst).difference(set(to_remove))))

# Approach2
lst = [10, 20, 30, 40, 50, 60]
to_remove = [20, 40, 60]

for elem in to_remove:
    lst.remove(elem)
else:
    print(f"lsit is: {lst}")


# Approach3
lst = [10, 20, 30, 40, 50, 60]
to_remove = [20, 40, 60]
new_lst = []
for elem in lst:
    if elem not in to_remove:
        new_lst.append(elem)
else:
    print(f"lst is :: {new_lst}")

# Approach4
lst = [10, 20, 30, 40, 50, 60]
to_remove = [20, 40, 60]
new_lst = [i for i in lst if i not in to_remove]
print(new_lst)

# Approach5 delete with indexes
lst = [10, 20, 30, 40, 50, 60]
to_remove_with_index = [1, 3, 4]
new_lst = []
for i, v in enumerate(lst):
    if i not in to_remove_with_index:
        new_lst.append(v)
else:
    print(f"{new_lst}")
    

# Approach6 delete with indexes
lst = [10, 20, 30, 40, 50, 60]
to_remove_with_index = [1, 3, 4]
new_lst = [v for i, v in enumerate(lst) if i not in to_remove_with_index]
print(new_lst)

