a=int(input("get num1:"))
b=int(input("get num2:"))
for i in range( min(a, b) ,0,-1):
        if a % i == 0 and b % i == 0:
            lcm_value = i
        else:
              continue
           
        
print("lcm:",lcm_value) 