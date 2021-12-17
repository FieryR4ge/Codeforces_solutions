# simple solution
# print([1, 2, 6, 20, 70, 252, 924, 3432, 12870, 48620][int(input()) - 1])

import math

n = int(input())

print(math.factorial(2*n-2)//(math.factorial(n-1)**2))
