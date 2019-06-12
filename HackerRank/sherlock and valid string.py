'''
Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur 
the same number of times. Given a string S, determine if it is valid. If so, return YES, otherwise return NO.
Sample Input 0
aabbcd
Sample Output 0
NO
Explanation 0
Given S="aabbcd, we would need to remove two characters, both c and d  aabb or a and b abcd, to make it valid. 
We are limited to removing only one character, so  is invalid.

Sample Input 1
aabbccddeefghi
Sample Output 1
NO
Explanation 1
Frequency counts for the letters are as follows:
{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}
There are two ways to make the valid string:

Remove 4 characters with a frequency of 1:fghi.
Remove 5 characters of frequency 2:abcde.

Sample Input 2
abcdefghhgfedecba
Sample Output 2
YES
Explanation 2
All characters occur twice except for e which occurs 3 times. We can delete one instance of e
to have a valid string.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
s=input()
s=''.join(sorted(s))
res=0
l,j=[],{}
for i in s:
    res=s.count(i)
    if(res!=0):
        l.append(res)
        j[i]=res
    s=s.replace(i,"")

if((l.count(l[0]))==len(j)-1) or ((l.count(l[0]))==len(j)):
    print("YES")
else:
    print("NO")
    
    
