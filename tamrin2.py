import random
n=int(input("get lenght of array:"))
array=[]
for i in range(n):
    x=random.randint(10,50)
    array.append(x)
print("your array is:",array)
