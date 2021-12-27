t = int(input())

for _ in range(t):
    n = int(input())
    friends = list(map(int, input().split()))
    if sum(friends) % n != 0:
        print(-1)
    else:
        counter = 0
        candies = sum(friends) // n
        for friend in friends:
            if friend > candies:
                counter += 1

        print(counter)