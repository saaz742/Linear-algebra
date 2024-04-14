import numpy as np
# A=A0​+λA1​+μA2​+κA3​
# A0​​​=∑i=1n​(ui​−yi​)2               A0'=2u-2y
# A1​=∑i=1n​(yi​)2                  A1'=2y
# A2=∑i=2n​(yi​−yi−1​)2​             A2'=2a2ᵀa2y #Difference Matrix
# |a11 ... a1n|       |x1|    |0      |
# |.          |   *   |. |  = |x2-x1  |
# |.          |       |. |    |.      |
# |an1 ... ann|       |xn|    |xn-xn-1|
#   | 0  0  0|
# a2=|-1  1  0|
#   |0  -1  1|
# A3​=∑i=2n−1​(yi+1​−2yi​+yi−1​)2​     A3'=2a3ᵀa3y
#    |0  0  0  0|
# a3= |1 -2  1  0|
#    |0  1 -2  1|
#    |0  0  0  0|
# A'=2u-2y+2yλ+2AᵀAyμ+2AᵀAyκ
# A'=0=u-y+yλ+AᵀAyμ+AᵀAyκ -> max or min


def cal(n, u, y):
    A2, A3 = makeM(n, y)
    x = np.vstack((y, A2, A3))
    return np.linalg.lstsq(np.transpose(x), u-y)


def makeM(n, y):
    a2 = np.zeros((n, n), dtype=float)
    a3 = np.zeros((n, n), dtype=float)
    for i in range(n-2):
        a2[i+1][i+1] = 1
        a2[i+1][i] = -1
        a3[i+1][i+1] = -2
        a3[i+1][i] = 1
        a3[i+1][i + 2] = 1
    a2[n-1][n-1] = 1
    a2[n-1][n-2] = -1
    return np.matmul(a2.transpose(), a2).dot(y), np.matmul(a3.transpose(), a3).dot(y)


if __name__ == '__main__':
    n = int(input())
    u = np.array(list(map(float, input().split())))
    y = np.array(list(map(float, input().split())))
    res = cal(n, u, y)[0]
    for i in range(3):
        print(round(res[i]))
