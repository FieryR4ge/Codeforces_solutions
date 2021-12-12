n = int(input())

cards = list(map(int, input().split()))

friends = [0, 0]

for i in range(n):
    x = max(cards[0], cards[-1])
    friends[i % 2] += x
    cards.remove(x)

print(*friends)

