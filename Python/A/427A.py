a = int(input())
b = list(map(int, input().split()))

hired = undisclosed = 0

for el in b:
    if el > 0:
        hired += el
        continue
    if hired > 0 and el < 0:
        hired -= 1
        continue
    if el < 0:
        undisclosed += 1

print(undisclosed)