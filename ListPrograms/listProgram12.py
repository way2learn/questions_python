# Python program to find N largest elements from a list
# listProgram12.py

# Approach1
lst = [1, 2, 3, 4, 5, 6, 7, 8]
n = int(input("Enter no.of largest numbers: "))
print(sorted(lst)[::-1][:n])

# Approach2
lst = [1, 2, 3, 4, 5, 6, 7, 8]
n = int(input("Enter no.of largest numbers: "))
lst.sort()
print(lst[-1: -(n+1): -1])

# Approach3
lst = [8, 4, 29, 33, 66, 189, 1, 2, 7]
n = int(input("Enter no.of largest numbers: "))
for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
else:
    print(lst)
    print(lst[::-1][:n])

# Approach4
lst = [1, 2, 3, 4, 5, 6, 7, 8]
n = int(input("Enter no.of largest numbers: "))
lst.sort(reverse=True)
print(lst[0:n])