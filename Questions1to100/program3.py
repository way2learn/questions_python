# 3. Write a Python program to get the largest number from a list. 
# program3.py

# Approach1
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
largest = lst[0]
for elem in lst[1:]:
    if elem > largest:
        largest = elem
else:
    print(f"max is: {largest}")


# Approach2
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
for i in range(len(lst)):
    for j in range(0, len(lst) - 1 - i):
        if lst[j] < lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
else:
    print(lst[0])

# Approach3
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
lst.sort()
print(lst[-1])

# Approach4
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
lst.sort(reverse=True)
print(lst[0])

# Approach5
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
print(sorted(lst)[-1])

# Approach6
lst = [1, 100, 23, 304, -99, 0, 987, -110, 888]
print(max(lst))
