n, d = map(int, input().split())
songs = sum([int(i) for i in input().split()])

answer = songs + (n - 1) * 10

if answer > d:
    print("-1")
else:
    print((d-songs) // 5)
