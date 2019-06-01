#Circular Rotation Infytest5
'''
Sample Input 0

3 2 3
1 2 3
0
1
2
Sample Output 0

2
3
1
Explanation 0

After the first rotation, the array becomes[3,1,2] . 
After the second (and final) rotation, the array becomes[2,3,1].

Let's refer to the array's final state as arrayb=[2,3,1] . For each query, we just have to print the value of on a new line:
m=0 b[0]=2
m=1 b[1]=3
m=2 b[2]=1
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    o=[]
    for i in range(len(a)-k,len(a)):
        o.append(a[i])
    for i in range(0,len(a)-k):
        o.append(a[i])
    for i in queries:
        print(o[i])

if __name__ == '__main__':

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    circularArrayRotation(a, k, queries)

