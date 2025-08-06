# Python program to print all even numbers in a range
# listProgram16.py

# Approach1
print("Program to print the even numbers in a range")
start_num = int(input("start number: "))
end_num = int(input("end number: "))
even_nums = []
if start_num > end_num:
    print("Not a valid range, start should less than end numbers")
else:
    for i in range(start_num, end_num + 1):
        if i % 2 == 0:
            even_nums.append(i)
    else:
        print(f"Even numbers between {start_num} and {end_num} are: {even_nums}")

# Approach2
print("Program to print the even numbers in a range")
start_num = int(input("start number: "))
end_num = int(input("end number: "))
even_nums = list()
if start_num > end_num:
    print("Not a valid range, start should less than end numbers")
else:
    if start_num % 2 != 0:
        start_num += 1
    for i in range(start_num, end_num + 1, 2):
        even_nums.append(i)
    else:
        print(f"Evens b/w {start_num} and {end_num} are: {even_nums}")

# Approch3 using while loop
print("Program to print the even numbers in a range")
start_num = int(input("start number: "))
end_num = int(input("end number: "))
even_nums = list()
