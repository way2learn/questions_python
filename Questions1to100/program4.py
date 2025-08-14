# 4. Write a Python program to get the smallest number from a list.
# program4.py

# Approach1
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
small = lst[0]
for elem in lst[1:]:
    if elem < small:
        small = elem
else:
    print(f"max is: {small}")


# Approach2
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
for i in range(len(lst)):
    for j in range(0, len(lst) - 1 - i):
        if lst[j] < lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
else:
    print(lst[-1])

# Approach3
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
lst.sort()
print(lst[0])

# Approach4
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
lst.sort(reverse=True)
print(lst[-1])

# Approach5
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
print(sorted(lst)[0])

# Approach6
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
print(min(lst))
