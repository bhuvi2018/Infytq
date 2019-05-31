'''
The reverse and add function starts with a number, reverses its digits, and adds the reverse to the original. If the sum is not a palindrome (meaning it does not give the same number read from left to right and right to left), we repeat this procedure until it does.

For example, if we start with 195 as the initial number, we get 9,339 as the resulting palindrome after the fourth addition:

 195  786    1,473  5,214
 591  687    3,741  4,125
+___ +_____ +_____ +_____
786   1,473  5,214  9,339
This method leads to palindromes in a few steps for almost all of the integers. But there are interesting exceptions. 196 is the first number for which no palindrome has been found. It has never been proven, however, that no such palindrome exists. You must write a program that takes a given number and gives the resulting palindrome (if one exists) and the number of iterations/additions it took to find it. 
195
4 9339
'''

def pal(n,c):
    n=str(n)
    r=str(n)
    r=r[::-1]
    if (n==r):
        print(c,r)
        return 0
    else:
        c+=1
        n=int(n)+int(r)
        pal(n,c)
i=input()
pal(i,0)
    
