import numpy as np


def min_radius(matrix):
    mul = np.eye(n)
    res = np.zeros((n, n))
    for i in range(1, n):
        mul = np.matmul(mul, matrix)
        res += mul
        minr = find(res, n)
        if minr != -1:
            return minr, i
    return -1, -1


def find(matrix, n):
    mat = np.eye(n) + matrix
    for i in range(n):
        if(one(mat, n, i) == True):
            return i
    return -1


def one(matrix, n, j):
    for i in range(n):
        if(matrix[j][i] == 0):
            return False
    return True


if __name__ == '__main__':
    matrix = []
    n = int(input())
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    res = min_radius(np.array(matrix))
    print(res[0])
    print(res[1])
