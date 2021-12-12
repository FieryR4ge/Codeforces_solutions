import math

t = int(input())

for _ in range(t):
    n = int(input())
    k = math.ceil((2/3)*n)//2
    l = n - 2 * k
    print(l, k, sep=' ')

