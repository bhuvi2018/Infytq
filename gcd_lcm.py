#GCD
def gcd(a,b): 
    if(b==0): 
        return a 
    else:
        return gcd(b,a%b)
 
print ("The gcd of 60 and 48 is : ",end="") 
print (gcd(60,48)) 


def find_gcd(num1,num2):
    #start writing your code here
    if num1 > num2: 
        small = num2
    else: 
        small = num1 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 

num1=45
num2=9
print(find_gcd(num1,num2))


#LCM
def gcd(a,b): 
    if (a == b): 
        return a 
    if (a > b): 
        return gcd(a-b, b) 
          
    return gcd(a, b-a) 

def lcm(a,b): 
    return (a*b)//gcd(a,b) 
a = 15 
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))
