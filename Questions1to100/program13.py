# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 
# program13.py

# 3, 4, 6 --> 3 layers, 4 rows, 6 columns

array_3d = [[[ "*" for _ in range(6)] for _ in range(4)] for _ in range(3)]
for i, layer in enumerate(array_3d):
    print(f"layer {i+1}\n")
    for row in layer:
     print(row)
    print()
