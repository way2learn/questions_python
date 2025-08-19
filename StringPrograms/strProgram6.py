# Python – Words Frequency in String Shorthands
# strProgram6.py

# Approach1
input_str = "apple banana apple orange banana apple"
words = input_str.split()
words_count = {}
for word in words:
    if word not in words_count:
        words_count[word] = 1
    else:
        words_count[word] += 1
else:
    print(f"words count dict: {words_count}")
    print(f"*"*30)
    print("Word\t\t Word-Frequency")
    print(f"*"*30)
    for k, v in words_count.items():
        print(f"{k}\t\t{v}")
    else:
        print(f"*"*30)

# Approach2
from collections import Counter
input_str = "apple banana apple orange banana apple"
counts = Counter(input_str.split())
for k, v in counts.items():
    print(f"{k}\t\t{v}")
