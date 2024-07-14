import math
import os
import random
import re
import sys

def quickSort(arr):
    p = arr[0]  
    left = []
    equal = []
    right = []
    
    for num in arr:
        if num < p:
            left.append(num)
        elif num == p:
            equal.append(num)
        else:
            right.append(num)
    
    return left + equal + right

n = int(input())
arr = list(map(int, input().split()))

result = quickSort(arr)

print(' '.join(map(str, result)))
