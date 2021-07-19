a = int(input())

passengers = []

max_psg = 0
x = 0

for i in range(a):
    passengers.append(list(map(int, input().split())))

for k in passengers:
    x += k[1] - k[0]
    if x > max_psg:
        max_psg = x

print(max_psg)
