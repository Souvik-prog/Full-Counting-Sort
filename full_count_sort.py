#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    n = len(arr)
    result = [[] for _ in range(n)]
    for i in range(n//2):
        result[int(arr[i][0])].append('-')
    for i in range(n//2, n):
        result[int(arr[i][0])].append(arr[i][1])
    for s in result:
        if s:
            print(*s, end = ' ')
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
