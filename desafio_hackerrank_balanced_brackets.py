#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(string):
    abertos = []
    
    for i in string:
        if i == '{' or i == '[' or i == '(':
            abertos.append(i);
        elif len(abertos) == 0:
            return 'NO'
        elif i == '}':
            if abertos[-1] != '{':
                return 'NO'
            else:
                del abertos[-1]
        elif i == ']':
            if abertos[-1] != '[':
                return 'NO'
            else:
                del abertos[-1]
        elif i == ')':
            if abertos[-1] != '(':
                return 'NO'
            else:
                del abertos[-1]
                
    if len(abertos) == 0:
        return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    fptr = open(file_path, 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
