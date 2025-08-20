# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 
# program16.py
lst = [val*val for val in range(1, 30+1)]
new_lst = lst[:5] + lst[-5:]
print(new_lst)