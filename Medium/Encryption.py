#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s):
    s = ''.join(s.split(' '))

    row = math.floor(math.sqrt(len(s)))
    col = math.ceil(math.sqrt(len(s)))

    if (row * col) < len(s):
        row = row + 1

    mat = []

    for i in range(row):

        if len(s[i * col:(i + 1) * col]) == col:
            mat.append(s[i * col:(i + 1) * col])
        else:
            zero = col - len(s[i * col:(i + 1) * col])
            mat.append(s[i * col:(i + 1) * col] + ('0' * zero))

    words = []

    for k in range(col):

        letter = []
        for l in range(row):

            if mat[l][k] == '0':
                continue

            letter.append(mat[l][k])

        words.append(''.join(letter))

    return ' '.join(words)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()