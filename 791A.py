a = list(map(int, input().split()))

counter = 0

while a[0] <= a[1]:
    a[0] *= 3
    a[1] *= 2
    counter += 1

print(counter)
