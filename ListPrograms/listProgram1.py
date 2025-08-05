# Python program to interchange first and last elements in a list
# listProgram1.py

# Approach1
lst = [103, 43, 89, 72, 26, 11] # Input list
temp = lst[0]  # Using a temp varaible
lst[0] = lst[len(lst) - 1]
lst[len(lst) - 1] = temp

print(lst)

# Approach2
lst = [103, 43, 89, 72, 26, 11]
lst[0], lst[len(lst) - 1] = lst[len(lst) - 1], lst[0]  # Using posstive indexing, forward direction

print(lst)

# Approach3
lst = [103, 43, 89, 72, 26, 11]
lst[-len(lst)], lst[-1] = lst[-1], lst[-len(lst)] # Using negative indexing, forward direction
print(lst)

# Approach4, Can be done using predefined functions of list
lst = [103, 43, 89, 72, 26, 11]
first_element = lst.pop(0)
last_element = lst.pop()
lst.append(first_element) # add at the end
lst.insert(0, last_element) # add at the beginning
print(lst)



