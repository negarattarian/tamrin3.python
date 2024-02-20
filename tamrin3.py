import random
n=int(input("get lenght of array:"))
array=[]
for i in range(n):
    x=int(input("get index:"))
    array.append(x)
array.sort()
print("your array is:",array)
