'''
find the frequency of character in a string.

Input Format
String

Constraints
5< stringlength < 15

Output Format
character & count

Sample Input
welcome

Sample Output
c 1
e 2
l 1
m 1
o 1
w 1
'''

h=input()
m=set(h)
m=sorted(m)
for i in m:
    b=0
    for j in h:
        if(i==j):
            b+=1
    print(i,b)
