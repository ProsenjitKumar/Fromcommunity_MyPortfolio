# import numpy
# n = numpy.array([input().split() for _ in range(int(input().split()[0]))],int)
# print(numpy.mean(n,axis=1),numpy.var(n,axis=0),numpy.std(n),sep="\n")


import numpy as np

n,m = map(int, input().split())
b = []
for i in range(n):
    a = list(map(int, input().split()))
    b.append(a)

b = np.array(b)

np.set_printoptions(legacy='1.13')
print(np.mean(b, axis = 1))
print(np.var(b, axis = 0))
print(np.std(b))