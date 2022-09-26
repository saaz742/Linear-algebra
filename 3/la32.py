
import numpy as np
import sys
# def make(coefficient, k):
#     matrix = np.zeros((k, k), dtype=int)
#     for i in range(k-1):
#         for j in range(k):
#             if i+1 == j:
#                 matrix[i][j] = 1
#             else:
#                 matrix[i][j] = 0
#     for i in range(k):
#         matrix[k-1][i] = coefficient[i]
#     return matrix


def find(matrix, n, k, first):
    matrix = np.zeros((k, k), dtype=int)
    for i in range(k-1):
        for j in range(k):
            if i+1 == j:
                matrix[i][j] = 1
    for i in range(k):
        matrix[k-1][i] = coefficient[i]
    if n > k:
        for i in range(n - k):
            first = matrix.dot(first)
            first %= 10000019
        return first[k-1]
    else:
        return first[n-1]


if __name__ == '__main__':
    k, n = map(int, input().split())
    first = list(map(int, input().split()))
    coefficient = list(map(int, input().split()))
    #print(find(make(coefficient, k), n, k, first))
    sys.stdout.write(str(find(coefficient, n, k, first))+"\n")
    #os.write(find(coefficient, n, k, first))
    #print(find(coefficient, n, k, first))
