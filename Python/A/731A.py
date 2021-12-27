a_ord = 97
result = 0

for word in map(ord, input()):
    s = abs(a_ord - word)
    result += min(s, 26-s)
    a_ord = word

print(result)