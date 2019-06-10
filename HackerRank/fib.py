n=int(input())
t1=0
t2=1
for i in range(n):
    print(t1,end=" ")
    t3=t2+t1
    t1=t2
    t2=t3
