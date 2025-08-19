# 15. Write a Python program to shuffle and print a specified list.
# program15.py

# Approach1
import random
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(f"Given List: {lst}, Shuffled list is: {lst}")

# Approach2
lst = [1,3, 5, 6, 7, 8]
new_lst = random.sample(lst, len(lst))
print(f"{lst} :: {new_lst}")