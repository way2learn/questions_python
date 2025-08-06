# Python program to find second largest number in a list
# listProgram11.py

# Approach1
lst = [1, 2, 3, 4,5]
lst.sort()
print(lst[-2])

# Approach2
lst = [1, 2, 3, 4,5]
print(sorted(lst)[-2]) 

# Approach3
lst = [1, 2, 3, 4, 5]
largest = lst[0]
second_largest = float('-inf')

for i in range(2, len(lst)):
    if lst[i] > largest:
        second_largest = largest
        largest = lst[i]
    elif lst[i] > second_largest:
        second_largest = lst[i]
else:
    print(f"second largest number is: {second_largest}")

