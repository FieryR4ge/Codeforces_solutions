n = int(input())

for _ in range(n):
    players = list(map(int, input().split()))
    first = max(players[:2])
    second = max(players[2:])
    sorted_players = sorted(players, reverse=True)[:2]
    if first in sorted_players and second in sorted_players:
        print("YES")
    else:
        print("NO")