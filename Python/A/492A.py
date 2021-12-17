n = int(input())

h = 0
count = 0
while count <= n:
    h += 1
    count += h*(h+1)//2

print(h-1)


