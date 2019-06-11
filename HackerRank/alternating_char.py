'''
For example, given the strings=AABAAB, remove an A at positions 0 and 3 to make ABAB in 2 deletions.
Sample Input
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
Sample Output
3
4
0
0
4
Explanation

The characters marked red are the ones that can be deleted so that the string doesn't have matching consecutive characters.

'''

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    for j in s:
        c=0
        for i in range(0,len(j)-1):
            if(j[i]==j[i+1]):
                c+=1
        print(c)
    
    
q = int(input())
s=[]
for i in range(0,q):
        s.append(input())

alternatingCharacters(s)
