#!/bin/python3
from array import array
from audioop import reverse
import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def getArray(index, list):
    return list[index]

def getGroupedLevels(indexes):
    get_pair = 0
    count = 0
    current_level = indexes[get_pair]
    grouped_levels = [[indexes[0]]]
    
    while get_pair <= len(indexes):
        next_level = []
        for i in current_level:
            count += 1
            if i > 0:
                next_level = next_level + [getArray(get_pair + count, indexes)]
        
        count = 0
        if len(next_level) > 0:
            grouped_levels += [next_level]

        get_pair += 1
        if get_pair <= len(indexes) - 1:
            current_level = indexes[get_pair]
        else:
            break
    
    return grouped_levels

def levelOrder(grouped_levels):
    if not grouped_levels:
        return

    roots_left = []
    roots_right = []
    array_result = []
    
    for level in grouped_levels:
        for root in level:
            # Visita filho da esquerda.
            root_left = root[0] if root[0] > 0 else None
            if root_left:
                roots_left.append(root_left)

            # Visita filho da direita.
            root_right = root[1] if root[1] > 0 else None
            if root_right:
                roots_right.append(root_right)

    if len(roots_left) > 0 or len(roots_right) > 0:
        array_result = roots_left + [1] + roots_right

    return array_result

def swapNodes(indexes, queries):
    
    grouped_levels = getGroupedLevels(indexes)
    result = []

    for i in range(len(queries)):

        p = queries[i] - 1
            
        level = grouped_levels[p]
        changed = []
        for l in level:
            changed += [[l[1],  l[0]]]
        
        grouped_levels[p] = changed
    
        result.append(levelOrder(grouped_levels))

    return result


if __name__ == '__main__':
    fptr = open("C:\\Users\\eduarda.costa\\Documents\\Estudo_Arvores\\txts\\swap_nodes.txt", 'w')

    n = int(5)

    indexes = [[2,3], [-1,4], [-1,5], [-1, -1], [-1, -1] ]

    # for _ in range(n):
    #     indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(1)

    queries = [2]

    # for _ in range(queries_count):
    #     queries_item = int(input().strip())
    #     queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
