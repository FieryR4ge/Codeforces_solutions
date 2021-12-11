n = int(input())

for _ in range(n):
    k = str(input())
    press = len(k)
    print(10 * (int(k[0]) - 1) + press * (press + 1) // 2)