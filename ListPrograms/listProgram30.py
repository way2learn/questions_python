# Break a list into chunks of size N in Python
# listProgram30.py

lst = [1, 2, 3, 4, 5,6, 7, 8, 9]
chunks_size = int(input("How many chunks you want?: "))
chunk_lst = []
for i in range(0, len(lst), chunks_size):
    chunk_lst.append(lst[i:i + chunks_size])
else:
    print(f"{chunks_size} chunk's of a list is: {chunk_lst} ")
