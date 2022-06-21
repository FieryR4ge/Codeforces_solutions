t = int(input())
n = list(map(int, input().split()))

for i in range(t):
    print(min(abs(n[i] - n[(i + 1) % t]), abs(n[i] - n[(i - 1) % t])), max(abs(n[i] - n[0]), abs(n[i] - n[-1])))