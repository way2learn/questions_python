# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). 
# program17.py

lst = [val * val for val in range(1, 31)]
new_lst = lst[5:]
print(new_lst)