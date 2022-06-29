for i in range(int(input())):
    t = int(input())
    tetris = sum(list(map(lambda x: int(x) % 2, input().split())))
    print("YES" if tetris == 0 or tetris == t else "NO")
