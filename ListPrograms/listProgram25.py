# Python | Count occurrences of an element in a list
# listProgram25.py

# Approach1
lst = [1, 2, 3, 4 ,5 , 6, 7, 8, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1 ,2, 3]
print(f"no.of 2 occurences in a list is: {lst.count(2)}")

# Approach2
lst = [1, 2, 3, 4 ,5 , 6, 7, 8, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1 ,2, 3]
occurences = 2
count = 0
for elem in lst:
    if elem == occurences:
        count += 1
else:
    print(f"No.Of occurences of {occurences} in a list: {count}")

