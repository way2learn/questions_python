# Python program to print all odd numbers in a range
# listProgram17.py

print("Program to Print the odd numbers in. a range")
start = int(input("Enter the first number in a range: "))
end = int(input("Enter a end number in a range: "))
odd_nums = []
for i in range(start, end + 1):
    if i % 2 != 0:
        odd_nums.append(i)
else:
    print(f"odd nums between {start} & {end} are: {odd_nums}")

# Approach2
print("Program to Print the odd numbers in. a range")
start = int(input("Enter the first number in a range: "))
end = int(input("Enter a end number in a range: "))
odd_nums = []
if start % 2 == 0:
    start += 1
for i in range(start, end + 1, 2):
    odd_nums.append(i)
else:
    print(f"odd nums between {start} and {end} are: {odd_nums}") 