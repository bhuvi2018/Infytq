i=int(input())
f=0
d=int(input())
while (i>0):
    r=i%10
    if r==d:
        print("digit found")
        f=1
        break
    i=i//10
if(f==0):
    print("digit not found")
