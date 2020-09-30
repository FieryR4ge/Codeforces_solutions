a = int(input())
j = 0
k = 0

while (k < a):
    n = str(input())
    if n.count('1') >= 2:
        j += 1
        k += 1
    else:
        k += 1
print(j)