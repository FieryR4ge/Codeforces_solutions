a = list(map(int, input().split()))
b = str(input())

while a[1]:
    b = b.replace("BG", "GB")
    a[1] -= 1

print(b)
