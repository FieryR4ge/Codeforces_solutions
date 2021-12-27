n = int(input())

h = 0
count = 0
while h <= n:
    count += 1
    h += count * (count + 1) // 2

print(count - 1)


