
a=int(input("get num1:"))
b=int(input("get num2:"))
for i in range(1, min(a, b)+1 ):
        if a % i == 0 and b % i == 0:
            gcd_value = i
        else:
              continue
           
        
print("gcd:",gcd_value)    
    