n = int(input())

for _ in range(n):
    length = int(input())

    l = length // 2

    # If half length is not even, prints NO
    if l % 2 != 0:
        print("NO")

    else:
        # Collecting 2 lists with even and odd numbers
        even = [2 * (i + 1) for i in range(l)]
        odd = [1 + 2 * i for i in range(l - 1)]

        # Result is concatenation of even, odd and difference between sum of even and odd
        result = even + odd + [sum(even) - sum(odd)]
        print(result)

        print("YES")
        print(" ".join(map(str, result)))
