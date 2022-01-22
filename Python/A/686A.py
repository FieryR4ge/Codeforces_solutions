n, x = map(int, input().split())

sad = 0

for _ in range(n):
    sign, qty = map(str, input().split())

    if sign == '-':
        if x - int(qty) >= 0:
            x -= int(qty)
        else:
            sad += 1
    else:
        x += int(qty)

print(x, sad)
