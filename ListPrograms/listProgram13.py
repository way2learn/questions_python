# Python program to find N Smallest elements from a list
# listProgram13.py

# Approach1
lst = [20, -30, 10, 2, 3, 45, -3]
n = int(input("Enter how many largest numbers you want: "))
print(F"{sorted(lst)[0:n]}")

# Approach2
lst = [20, -30, 10, 2, 3, 45, -3]
n = int(input("Enter how many largest numbers you want: "))
lst.sort()
print(f"{lst[0:n]}")

# Approach3
lst = [20, -30, 10, 2, 3, 45, -3]
n = int(input("Enter how many largest numbers you want: "))
for i in range(0, len(lst)):
    for j in range(0, len(lst) - 1 - i):
        if lst[j] > lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
else:
    print(f"{lst}")
    print(f"{lst[0:n]}")
