num = int(input())
count =int(0)
sum=int(0)
rev=int(0)
while(num!=0):
    rem=int(num%10)
    count+=1
    num=num//10
    sum+=rem
    rev=int(rev*10)+rem
print("REVERSE is ",rev)
print("SUM is ",sum)
print("COUNT is",count)
