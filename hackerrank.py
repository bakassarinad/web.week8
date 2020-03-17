# 1 
print("Hello, World!")
# 2 
#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    if n % 2 == 0 and n in range(2, 6):
        print("Not Weird")
    if n in range(6, 21) and n % 2 == 0:
        print("Weird")
    if n > 20 and n % 2 == 0:
        print("Not Weird")
# 3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
# 4
from __future__ import division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
# 5
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)
# 6
def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        leap = True

    # Write your logic here
    
    return leap
# 7
from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")
# 8
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(ans)
# 9
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    first = second = -2147483648
    for i in range(len(arr)):
            if(arr[i] > first):
                second = first
                first = arr[i]
            elif arr[i] > second and arr[i] != first:
                second = arr[i]
        
    print(second)
# 10
if __name__ == '__main__':
    N = int(input())
mini = 101
mini2 = 102
a = []

for i in range(N):
    name = input()
    mark = float(input())
    if mark<mini:
        mini2 = mini
        mini = mark
    elif mark!=mini and mark<mini2:
        mini2 = mark
    a.append([name, mark])
    
b = [x[0] for x in a if x[1]==mini2]
b.sort()
for y in b:
    print(y)