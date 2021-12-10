n = int(input())

for i in range(n):
    k = int(input())
    word = list(input())
    word_copy = word.copy()

    for j in range(k - 1):
        if word[j] == word[j+1]:
            word_copy.remove(word[j+1])

    if len(word_copy) != len(set(word_copy)):
        print("No")
    else:
        print("Yes")
