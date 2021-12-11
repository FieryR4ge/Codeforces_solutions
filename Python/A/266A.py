qty = int(input())
stones = str(input())
counter = 0

for i in range(len(stones)):
    if i == len(stones) - 1:
        break
    if stones[i] == stones[i + 1]:
        counter += 1

print(counter)
