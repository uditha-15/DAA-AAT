import math
import os
import random
import re
import sys

def unboundedKnapsack(k, arr):
    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        for weight in arr:
            if weight <= i:
                dp[i] = max(dp[i], dp[i - weight] + weight)  
    return dp[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    results = []
    for _ in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        arr = list(map(int, input().rstrip().split()))
        result = unboundedKnapsack(k, arr)
        results.append(result)
    for result in results:
        fptr.write(str(result) + '\n')
    fptr.close()
