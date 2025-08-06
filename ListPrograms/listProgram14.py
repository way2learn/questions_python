# Python program to print even numbers in a list
# listProgram14.py

# Approach
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even_num_list = []
for item in lst:
    if item % 2 == 0:
        even_num_list.append(item)
else:
    print(f"Even List is {even_num_list}")


# Approach2
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even_num_list = []
for i in range(0, len(lst)):
    if lst[i] % 2 == 0:
        even_num_list.append(lst[i])
else:
    print(f"even num list: {even_num_list}")

# Approch3
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 55, 66, 12]
even_num_list = []
i = 0
while i < len(lst):
    if lst[i] % 2 == 0:
        even_num_list.append(lst[i])
    i += 1
else:
    print(f"even numbers list: {even_num_list}")