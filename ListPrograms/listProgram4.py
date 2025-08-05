# Python | Ways to check if element exists in list
# listProgram4.py


# num = int(input("Enter a num to creqte a list: "))
# if num <= 0:
#     print("Invalid Num")
# else:
#     lst = []
#     for i in range(1, num + 1):
#         value = int(input(f"Enter the list's {i} elements: "))
#         lst.append(value)
#     else:
#         print(f"created a list is: {lst}")

# Approach1 - using membership and ternery operators
lst = [1, 2, 3, 4 ,5]
elem = 4
elem_is_exist = True if elem in lst else False
if elem_is_exist:
    print(f"{elem} is exist in a given list")
else:
    print(f"{elem} is not exist in a given list")

# Approach2 using for loop and break statement
lst = [1, 2, 3, 4 ,5]
find_elem = 3
for item in lst:
    if item == find_elem:
        print(f"{item} is exist in a given list")
        break
else:
    print(f"{find_elem} is not present in a give list")

# Approach3 using predeifned function count

lst = [1, 2, 3, 4 ,5]
find_elem = 32
lst.count(find_elem)
if lst.count(find_elem):
    print(f"{find_elem} is exist in a lst: {lst}")
else:
    print(f"{find_elem} is does not exist in a lst: {lst}")

# Appraoch4 using predefined function index

lst = [1, 2, 3, 4 ,5]
find_elem = 4
if lst.index(find_elem):
    print(f"{find_elem} is exist in a {lst}")