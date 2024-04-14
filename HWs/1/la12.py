import numpy as np

v = np.array(input().split(), dtype='int')


def sum(v):
    return np.sum(v)


def sumOfOlder(v):
    return (np.sum(v[61:]))


def avg(v):
    return np.dot(np.arange(100), v)/np.sum(v)


def mode(v):
    return np.argmax(v)


print(format(sum(v), '.2f'))
print(format(sumOfOlder(v), '.2f'))
print(format(avg(v), '.2f'))
print(format(mode(v),  '.2f'))
