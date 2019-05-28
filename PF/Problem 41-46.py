#PF-Tryout 46

def doublePreceding (values):
    if len(values) > 0:
        previous = values[0]
        values[0] = 0
        for idx in range(1, len(values)):
            previous1 = values[idx]
            values[idx] = 2 * previous
            previous=previous1
    return values
    
print(doublePreceding([3,8,2]))


#46_hackerrank
b=input()
b=b.split(" ")
def double(v):
    if len(v) > 0:
        pre = int(v[0])
        v[0] = 0
        for i in range(1, len(v)):
            temp=int(v[i])
            v[i] = 2 * int(pre)
            pre = temp
    return v
bb=double(b)
for i in bb:
    print(i,end=" ")
