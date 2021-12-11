n = int(input())

print(n//2)

if n % 2 == 0:
    for i in range(n//2):
        print(2, end=' ')
else:
    for i in range(n//2-1):
        print(2, end=' ')
    print(3)
