import math
t = input()
t = int(t)
for _ in range(t):
    n = input()
    n = int(n)
    s = int(math.pow(2,math.floor(math.log(n,2))))
    k = n - s
    print(1+(k)*2)