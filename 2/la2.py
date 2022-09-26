import numpy as np


def gs(matrix):
    basis = []
    matrix = np.array(matrix)
    for i in matrix:
        q = i - np.sum(np.dot(i, b)*b for b in basis)
        if (q > 1e-4).any():
            basis.append(q/np.linalg.norm(q))
    return np.array(basis)


def swap(matrix, r1, r2, c):
    for i in range(c):
        t = matrix[r1][i]
        matrix[r1][i] = matrix[r2][i]
        matrix[r2][i] = t


def rank(matrix):
    r = len(matrix)
    if r == 0:
        c = 0
    else:
        c = len(matrix[0])
    rank = min(r, c)
    for i in range(rank):
        if matrix[i][i] != 0:
            for j in range(r):
                if j != i:
                    mul = (matrix[j][i] / matrix[i][i])
                    for k in range(rank):
                        matrix[j][k] -= (mul * matrix[i][k])
        else:
            minus = True
            for j in range(i + 1, r, 1):
                if matrix[j][i] != 0:
                    swap(matrix, i, j, rank)
                    minus = False
                    break
            if minus:
                rank -= 1
                for j in range(0, r, 1):
                    matrix[j][i] = matrix[j][rank]
            i -= 1
    return rank


if __name__ == '__main__':
    matrix = []
    m, n = map(int, input().split(' '))
    for i in range(m):
        r = map(int, input().split(' '))
        matrix.append(list(r))
    matrix = np.array(matrix).transpose()
    print(rank(gs(matrix)))
