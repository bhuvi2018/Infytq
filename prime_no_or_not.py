num=int(input())
if num > 1: 
      
   # Iterate from 2 to n / 2  
   for i in range(2, num//2): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 



#prime number in a range

lower=int(input())
upper=int(input())

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num//2):
           if (num % i) == 0:
               break
       else:
           print(num)
