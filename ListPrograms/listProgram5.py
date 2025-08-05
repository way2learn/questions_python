# Different ways to clear a list in Python
# listProgram5.py

# Approach1 using clear predefined function
lst = [1, 2, 3]
lst.clear()
print(lst)

# Approach2 using []
lst = [1, 2, 4 ,5, 6]
if len(lst):
    lst = []

print(lst)

# Approach3 
lst = [1, 2, 4 ,5, 6]
for i in range(0, len(lst)):
    lst.pop()
else:
    print(f"lst is  cleared using for loop and pop function {lst}")

# Approach4
lstt = [1, 2, 3, 4]
for elem in lstt[::-1]:
    lstt.remove(elem)
else:
    print(f"list is cleared using remove function {lstt}")

# Approach5
lst = [1, 2, 3,3, 4]
while True:
    if lst:
        lst.pop()
    else:
        print(f"Givenn list is empty {lst}")
        break

# Approach6
lst = [1, 2, 3,3, 4]
while lst:
    lst.pop()
else:
    print(f"list is empty {lst}")