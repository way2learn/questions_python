# Python | Cloning or Copying a list
# listProgram24.py

# Approach1
lst = [1, 2, 3, 4, 5]
print(lst, id(lst))
new_lst = lst.copy()
print(new_lst, id(new_lst))

# Approach2
lst = [1, 2, 3, 4, 5]
new_lst = []
print(lst, id(lst))
for elem in lst:
    new_lst.append(elem)
else:
    print(f"new lst: {new_lst}, {id(new_lst)}")
