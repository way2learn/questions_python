# Python program to print odd numbers in a List
# listProgram15.py

# Approach1
lst = [-22, -9, -6, -44, -43, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 55, 66, 12]
odd_elem_list = []
for elem in lst:
    if elem % 2 != 0:
        odd_elem_list.append(elem)
else:
    print(f"Odd list: {odd_elem_list}")

# Approach2
lst = [-22, -9, -6, -44, -43, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 55, 66, 12]
odd_elem_list = []
for i in range(0, len(lst)):
    if lst[i] % 2 != 0:
        odd_elem_list.append(lst[i])
else:
    print(f"odd elems list is: {odd_elem_list}")

# Approach3 using while loop
lst = [-22, -9, -6, -44, -43, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 55, 66, 12]
i = 0
odd_elem_list = []
while i <= len(lst) - 1:
    if lst[i] % 2 != 0:
        odd_elem_list.append(lst[i])
    i += 1
else:
    print(f"odd elems list: {odd_elem_list}")

