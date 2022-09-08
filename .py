#!/bin/python3

import math
import os
import random
import re
import sys


import numpy as np
#
# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimalHeaviestSetA(arr):
    pesos = arr
    qtd_pesos_a = len(arr) % 2

    max = np.max(pesos)
    
    a = []
    a.append(max)
    pesos.remove(max)
    
    while len(a) > qtd_pesos_a:
        for i in range(len(pesos)):
            if sum(a) + i > sum(pesos) - i:
                a.append(i)
    
    return a
        

    
if __name__ == '__main__':
    fptr = open(file_path, 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minimalHeaviestSetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
