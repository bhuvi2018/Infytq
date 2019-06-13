'''
Sample Input
5 2  
1 5 3 4 2  
Sample Output
3
Explanation
There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1] .
'''
import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k,s):
    c=0
    s=set(s)
    for i in s:
        if i+k in s:
            c=c+1
    return c
        
        
nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().split()))
print(pairs(k,arr))
