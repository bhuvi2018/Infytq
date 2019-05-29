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

    
#digits counting
i=int(input())
f=0
c=0
d=int(input())
while (i>0):
    r=i%10
    if r==d:
        c+=1
        f=1
    i=i//10
if(f==0):
    print("digit not found")
else:
    print("digit's count:",c)


#frst digit of a no
i=int(input())
while (i>0):
    r=i%10
    i=i//10
    
print(r)

#alternate
a=input()
print(a[0])
