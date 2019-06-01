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
