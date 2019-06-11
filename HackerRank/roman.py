#num to roman 1
def num_to_roman(num):
    num_list = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
    symbol_list = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    roman =''
    i = 0
    if num <5000:
        while  num > 0:
            for _ in range(num // num_list[i]):
                roman += symbol_list[i]
                num -= num_list[i]
            i +=1
    return roman
    
number = int(input())
print(num_to_roman(number))

# 2
n=int(input())
def roam(n):
    m=["", "M", "MM", "MMM","MMMM"]
    c=["", "C", "CC", "CCC", "CD", "D","DC", "DCC", "DCCC", "CM"]
    x=["", "X", "XX", "XXX", "XL", "L","LX", "LXX", "LXXX", "XC"]
    i=["", "I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX"]
    thousands=m[n//1000]
    hundreds=c[(n%1000)//100]
    tens=x[(n%100)//10]
    ones=i[n%10]
    print(thousands+hundreds+tens+ones)
roam(n)

#roman to number 1
def rom_to_int(s):

    t=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],
    ['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    r=0
    for p in t:
        c=True
        while c:
            if len(s)>=len(p[0]):
                if s[0:len(p[0])]==p[0]:
                    r+=p[1]
                    s=s[len(p[0]):]
                else: break
            else: break

    return r
print(rom_to_int("MMMDCCLVI"))

#roman - number
def v(s):
    if s=="I":
        return 1
    if s=="V":
        return 5
    if s=="X":
        return 10
    if s=="L":
        return 50
    if s=="C":
        return 100
    if s=="D":
        return 500
    if s=="M":
        return 1000
    return -1
def r(ss):
    q=0
    i=0
    while(i<len(ss)):
        s1=v(ss[i])
        if(i+1<len(ss)):
            s2=v(ss[i+1])
            if s1>=s2:
                q+=s1
                i=i+1
            else:
                q+=s2-s1
                i=i+2
        else:
            q+=s1
            i=i+1
    return q

m=input()
print(r(m))
