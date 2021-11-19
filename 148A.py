suffered = [int(input()) for i in range(4)]
dragons = int(input())
# check every dragons quantity % every suffered number == 0 and making set to remove duplicates
s = set([i for i in range(1, dragons + 1) for j in suffered if i % j == 0])
# length of set is the answer
print(len(s))
