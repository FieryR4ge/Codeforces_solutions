a = int(input())

if a <= 5:
    print(1)
elif a % 5 == 0:
    print(a//5)
else:
    x = a // 5
    print(x+1)
