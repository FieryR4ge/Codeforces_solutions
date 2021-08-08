n = int(input())

number = 0

for i in range(n):
    a = list(map(int, input().split()))
    if a[1] - a[0] >= 2:
        number += 1

print(number)
