# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
# program11.py

# Approach1
def common_elem_check(lst1, lst2):
    for elem in lst1:
        if elem in lst2:
            print(elem)
            return True
    return False

if __name__ == "__main__":
    res = common_elem_check([1, 2, 3], [4, 5, 6, 7])
    if res:
        print(f"{bool(1)}")
    else:
        print(f"{bool("")}")

# Approach2
