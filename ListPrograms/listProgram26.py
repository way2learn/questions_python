# Python | Remove empty tuples from a list
# listProgram26.py

# Approach1
lst = [1, 2, 3, 4, [1, 2], (), (1, 2, 3, 4), (), {1:"one", 2:"Two"}]
for elem in lst:
    if elem == ():
        lst.remove(elem)
else:
    print(f"list after removal: {lst}")

# Approach2
lst = [1, 2, 3, 4, [1, 2], (), (1, 2, 3, 4), (), {1:"one", 2:"Two"}]
for i in range(lst.count(())):
    lst.remove(())
else:
    print(f"list after removal: {lst}")

# Approach3
lst = [1, 2, 3, 4, [1, 2], (), (1, 2, 3, 4), (), {1:"one", 2:"Two"}]
for i in range(lst.count(())):
    lst.pop(lst.index(()))
else:
    print(f"list after removal: {lst}")
        