a, b = map(int, input().split())


def count_shovels(shovel_price: int, coin: int) -> int:

    for i in range(1, 11):
        if (i * shovel_price) % 10 in [0, coin]:
            break

    return i


print(count_shovels(a, b))
