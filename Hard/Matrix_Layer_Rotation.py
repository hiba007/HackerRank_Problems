#!/bin/python3

import math
import os
import random
import re
import sys
import copy


#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(arr, r):
    # Write your code here

    rows = len(arr)

    cols = len(arr[1])

    arr1 = copy.deepcopy(arr)

    for rotate in range(r):

        if rows == cols:

            k = 0

            while True:

                if (cols - 1) - k <= k and (rows - 1) - k <= k:
                    break

                for i in range(k, rows - k):

                    if i == k:
                        arr1[k][k] = arr[k][k + 1]

                    else:

                        arr1[i][k] = arr[i - 1][k]

                        arr1[i - 1][cols - (1 + k)] = arr[i][cols - (1 + k)]

                        if i >= (cols - k):
                            continue

                        arr1[rows - (1 + k)][i] = arr[rows - (1 + k)][i - 1]

                        arr1[k][i - 1] = arr[k][i]

                arr = copy.deepcopy(arr1)

                k += 1

        if rows > cols:

            k = 0

            while True:

                if (cols - 1) - k <= k <= (rows - 1) - k:
                    break

                for i in range(k, rows - k):

                    if i == k:
                        arr1[k][k] = arr[k][k + 1]

                    else:

                        arr1[i][k] = arr[i - 1][k]

                        arr1[i - 1][cols - (1 + k)] = arr[i][cols - (1 + k)]

                        if i >= (cols - k):
                            continue

                        arr1[rows - (1 + k)][i] = arr[rows - (1 + k)][i - 1]

                        arr1[k][i - 1] = arr[k][i]

                arr = copy.deepcopy(arr1)

                k += 1

        if cols > rows:

            k = 0

            while True:

                if (cols - 1) - k >= k >= (rows - 1) - k:
                    break

                for i in range(k, cols - k):

                    if i == k:
                        arr1[k][k] = arr[k][k + 1]

                    else:

                        arr1[rows - (1 + k)][i] = arr[rows - (1 + k)][i - 1]
                        arr1[k][i - 1] = arr[k][i]

                        if i >= (rows - k):
                            continue

                        arr1[i][k] = arr[i - 1][k]

                        arr1[i - 1][cols - (1 + k)] = arr[i][cols - (1 + k)]

                arr = copy.deepcopy(arr1)

                k += 1

    for j in range(rows):
        print(' '.join(str(num) for num in arr1[j]))


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)