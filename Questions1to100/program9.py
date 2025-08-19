# 9. Write a Python program to clone or copy a list.
# program9.py

# Approach1
lst = [1, 2, 3,4 , 5]
new_lst = lst.copy() # here copy follows shallow copy
print(f"{lst} and type is: {type(lst)}, id is: {id(lst)} \n new_list: {new_lst}, type: type{type(new_lst)}, id is: {id(new_lst)}")

# Approach2
lst2 = [1, 2, 3,4 , 5]
new_lst2 = [x for x in lst]
print(f"{lst2} and type is: {type(lst2)}, id is: {id(lst2)} \n new_list: {new_lst2}, type: type{type(new_lst2)}, id is: {id(new_lst2)}")
