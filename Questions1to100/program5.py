# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
#		Sample List : ['abc', 'xyz', 'aba', '1221']
#		Expected Result : 2
# program5.py
lst = ['abc', 'xyz', 'aba', 2,'1221']
count = 0
strs = []
for elem in lst:
    if isinstance(elem, str):
        if len(elem) >= 2 and elem[0] == elem[-1]:
            count += 1
            strs.append(elem)
    else:
        raise Exception(f"The list has non strings")
else:
    print(f"{lst} is the list, required list us {strs} and its count is {count}")