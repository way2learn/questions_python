# 7. Write a Python program to remove duplicates from a list. 
# program7.py

# Approach1
lst = [1, 2, 3, 4 ,5 ,6, 7, 1, 3, 4, 5]
duplicates = []
for val in lst:
    if val not in duplicates and lst.count(val) > 1:
        duplicates.append(val)
else:
    print(f"{duplicates}")

# Approach2
lst = [1, 2, 3, 4 ,5 ,6, 7, 1, 3, 4, 5]
s1 = set()
s2 = set()
for val in lst:
    if val not in s1:
        s1.add(val)
    else:
        s2.add(val)
else:
    print(f"unique s1: {s1}, duplicates s2: {s2}")

# Approach3
lst = [1, 2, 3, 4 ,5 ,6, 7, 1, 3, 4, 5]
l1 = list()
l2 = list()
for val in lst:
    if val not in l1:
        l1.append(val)
    else:
        l2.append(val)
else:
    print(f"unique l1: {l1}, duplicates l2: {l2}")

# Approach4
lst = [1, 2, 3, 4 ,5 ,6, 7, 1, 3, 4, 5, 1]
unique = list()
dup = list()
for val in lst:
    if val in unique and val not in dup:
        dup.append(val)
    elif val not in dup and val not in unique:
        unique.append(val)
else:
    print(f"unique l1: {unique}, duplicates l2: {dup}")
    from collections import Counter

    lst = [1, 2, 3, 4 ,5 ,6, 7, 1, 3, 4, 5, 1, 1, 1, 1,1]
    counts = Counter(lst)
    unique = []
    dup = []
    for val in lst:
        if counts[val] == 1:
            unique.append(val)
        elif counts[val] > 1 and val not in dup:
            dup.append(val)
    else:
        print(f"unique: {unique} and duplicates: {dup}")

# Approach5
from collections import Counter

lst = [1, 2, 3, 4, 5, 6, 7, 1, 3, 4, 5, 1, 1, 1, 1, 1]
counts = Counter(lst)

unique = []
dup = []
seen_dup = set()

for val in lst:
    if counts[val] == 1:
        unique.append(val)
    elif val not in seen_dup:
        dup.append(val)
        seen_dup.add(val)

print(f"Unique: {unique}")
print(f"Duplicates: {dup}")
print(f"seen {seen_dup}")