n = int(input())

scores = list(map(int, input().split()))

min_score, max_score = scores[0], scores[0]
counter = 0
for score in scores[1:]:
    if score > max_score:
        counter += 1
        max_score = score
    elif score < min_score:
        counter += 1
        min_score = score

print(counter)
