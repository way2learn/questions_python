# Python program to print all negative numbers in a range
# listProgram21.py


# Approach1
print("Program to print the positive numbers: ")
start = int(input("Enter the starting number of a range: "))
end = int(input("Enter the ending number of a range: "))
if start > end:
    print("Starting number should be less than secondary number")
else:
    negative_nums = []
    for i in range(start, end + 1):
        if i < 0:
            negative_nums.append(i)
    else:
        print(f"negative numbers between {start} & {end} are: {negative_nums}")

# Approch2
print("Program to print the positive numbers: ")
start = int(input("Enter the starting number of a range: "))
end = int(input("Enter the ending number of a range: "))
if start > end:
    print("Starting number should be less than secondary number")
else:
    negative_nums = [i for i in range(start, end + 1) if i < 0]
    print(f"negative numbers between {start} & {end} are: {negative_nums}")

