#PF-Prac-24
def find_gcd(num1,num2):
    if(num2==0): 
        return num1
    else:
        return find_gcd(num2,num1%num2)

num1=45
num2=9
print(find_gcd(num1,num2))
