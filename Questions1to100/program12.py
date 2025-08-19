# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
#		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#		Expected Output : ['Green', 'White', 'Black']
# program12.py 0 4 5

# Approach1
idx = [0, 4, 5]
sample_lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i in idx[::-1]:
    sample_lst.pop(i)
else:
    print(f"{sample_lst}")

# Approach2
idx = [0, 4, 5]
sample_lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
new_lst = [elem for i, elem in enumerate(sample_lst) if i not in idx]
print(new_lst)