i=1634
sum=0
rev=0
d=0
pr=1
t=i
s=0
while i>0:
    r=i%10
    d+=1
    i=i//10
    sum+=r
    s+=r**len(str(t)) 
    rev=rev*10+r
    pr*=r
print("Reverse :",rev)
print("Sum of digits:",sum)
print("No of Digits:",d)
print("Product :",pr)
if(rev==t):
    print("Palindrome")
else:
    print("Not Palindrome")
if(s==t):
    print("Amstrong number")
else:
    print("Not Amstrong number")
    
