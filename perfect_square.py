import math 
  
def isPerfectSquare(x): 
  
    # Find floating point value of  
    # square root of x. 
    sr = math.sqrt(x) 
    # If square root is an integer 
    return ((sr - math.floor(sr)) == 0) 
  
x = 49
if (isPerfectSquare(x)): 
    print("Yes") 
else: 
    print("No") 
    
    
#Perfect square in a limit

def squares(a, b):
    lists=[]
    # Traverse through all numbers
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
print(squares(15, 30))



