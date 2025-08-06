# Python program to print all positive numbers in a range

# listProgram20.py

# Approach1
print("Program to print the positive numbers: ")
start = int(input("Enter the starting number of a range: "))
end = int(input("Enter the ending number of a range: "))
if start > end:
    print("Starting number should be less than secondary number")
else:
    positive_nums = []
    for i in range(start, end + 1):
        if i > 0:
            positive_nums.append(i)
    else:
        print(f"Postive numbers between {start} & {end} are: {positive_nums}")

# Approch2
print("Program to print the positive numbers: ")
start = int(input("Enter the starting number of a range: "))
end = int(input("Enter the ending number of a range: "))
if start > end:
    print("Starting number should be less than secondary number")
else:
    positive_nums = [i for i in range(start, end + 1) if i > 0]
    print(f"Postive numbers between {start} & {end} are: {positive_nums}")

