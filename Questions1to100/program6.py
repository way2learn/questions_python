# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
#	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# program6.py

# Approach1
num = int(input("How many tuple's of elements you want in a list: "))
if num <= 1:
    print("Invallid number, Should be greater than 1")
else:
    lst = []
    for i in range(num):
        lst_elem = input(f"Enter the {i+1} tuple element, Ex: 1, 2:: ")
        lst.append(tuple(map(int, lst_elem.strip().split(',')))) 
    else:
        print(f"lst is: {lst}")     
        for i in range(len(lst)):
            for j in range(len(lst) - i - 1):
                if lst[j][1] > lst[j+1][1]:
                    temp = lst[j]
                    lst[j] = lst[j+1]
                    lst[j+1] = temp
        else:
            print(f"sorted lst is based on last elem of tpl: {lst}")

# Approach2
num = int(input("How many tuple's of elements you want in a list: "))
if num <= 1:
    print("Invalid number, Should be greater than 1")
else:
    lst = []
    for i in range(num):
        lst_elem = input(f"Enter the {i+1} tuple element, Ex: 1, 2:: ")
        tpl = tuple([int(x.strip()) for x in lst_elem.strip().split(",")])
        lst.append(tpl)
    else:
        print(f"lst: {lst}")
        print(f"sorted as required: {sorted(lst, key=lambda elem : elem[-1])}")
