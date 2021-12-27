from typing import List

a = str(input())

cards = list(map(str, input().split()))


def solve(array_cards: List) -> str:
    for card in array_cards:
        if a[0] == card[0] or a[1] == card[1]:
            return "YES"

    return "NO"


print(solve(cards))
