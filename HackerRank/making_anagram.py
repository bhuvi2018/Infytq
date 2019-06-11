'''
Sample Input
cde
abc

Sample Output
4

Explanation
We delete the following characters from our two strings to turn them into anagrams of each other:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
We had to delete 4 characters to make both strings anagrams.

'''
import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    d=len(s1)+len(s2)
    c=0
    for i in s1:
        if(i in s2):
            a=s1.count(i)
            b=s2.count(i)
            if(a>b):
                e=b
            else:
                e=a
            c+=e+e
            s1=s1.replace(i,'')
            s2=s2.replace(i,'')
    print(d-c)

s1 = input()
s2 = input()
makingAnagrams(s1, s2)
