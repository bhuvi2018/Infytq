i=input()
k=len(i)
s=int(0)
for j in range(0,k):
    s+=int(i[j])**k
if(int(i)==s):
    print("Yes")
else:
    print("No")
