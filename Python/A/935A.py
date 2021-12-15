l = int(input())
a = 1

for i in range(2, l):
    if l % i == 0:
        a += 1

print(a)
