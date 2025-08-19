# 10. Write a Python program to find the list of words that are longer than n from a given list of words. 
# program10.py
# Approach1
print("Enter a words saperated by space to find the words longer than 5: ")
lst_words = [word for word in input().split() if len(word) > 5]
print(f"{lst_words}")


# Approach2
print("Enter a words saperated by space to find the words longer than 5: ")
words = input().split()
lst_words = list(filter(lambda x : len(x) > 5, words))
print(lst_words)