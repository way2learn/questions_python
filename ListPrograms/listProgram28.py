# Python program to find Cumulative sum of a list
# listProgram28.py

# Approach1
lst = [1, 2, 3, 4 ,5]
cummulative_sum = []
sum = 0
for elem in lst:
    sum += elem
    cummulative_sum.append(sum)
else:
    print(f"cummulative_sum is: {cummulative_sum}")