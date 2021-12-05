n = int(input())

for _ in range(n):
    length = int(input())

    l = length // 2
    if l % 2 != 0:
        print("NO")

    else:
        even = [2 * (i + 1) for i in range(l)]
        odd = [1 + 2 * i for i in range(l - 1)]
        # print(f"Even: {even}")
        # print(f"Odd: {odd}")
        result = even + odd + [sum(even) - sum(odd)]

        print("YES")
        print(" ".join(map(str, result)))
