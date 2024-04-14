import numpy as np

np.set_printoptions(precision=4)

a = np.array(input().split(), dtype='int')
b = np.array(input().split(), dtype='int')
c = np.array(input().split(), dtype='int')


def unitVector(vector):
    return vector / np.linalg.norm(vector)


def angle(v1, v2):
    return np.arccos(np.clip(np.dot(unitVector(v1), unitVector(v2)), -1.0, 1.0))


def vertical(v1, v2):
    return np.float32(np.cross(v1, v2) / np.linalg.norm(np.cross(v1, v2)))


def area(v1, v2):
    ang = angle(v1, v2)
    return np.linalg.norm(v1) * np.linalg.norm(v2) * np.sin(ang)


def block(v1, v2, v3):
    return np.int32(np.block([v1, v2, v3]))


def matrix(v1, v2, v3):
    return np.matrix([v1, v2, v3], dtype='int32')


print(format(angle(a, b), '.2f'))
print(vertical(a, c))
print(format(area(a, b), '.2f'))
print(block(a, b, c))
print(matrix(a, b, c))
