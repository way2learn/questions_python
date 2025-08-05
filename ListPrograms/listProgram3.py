# Python | Ways to find length of list
# listProgram3.py

# Approach1 using len function
lst = [1, 2, 3, 4]
print(f"lst len is {len(lst)}")


# Appraoch2 using for loop
lst = [1, 2, 3, 4]
i = 0
for char in lst:
    i += 1
else:
    print(f"lst length is: {i}")

# Appraoch3 using while loop

lst = [1, 2, 3, 4]
i = 0
while lst[i]:
    i += 1
else:
    print(f"lst lenght is: {i}")
    