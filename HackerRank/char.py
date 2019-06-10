'''
Remove all Characters in a String except Alphabet.

Input Format
String

Constraints
2 < String Length < 15

Output Format
String

Sample Input
kitcse12

Sample Output
kitcse

Explanation
Remove all Characters in a String except Alphabet.
'''

s=input()
k=[]
for i in range(0,len(s)):
    if(s[i]>="a" and s[i]<="z" or s[i]>="A" and s[i]<="Z"):
        k.append(s[i])
for i in k:
    print(i,end="")
