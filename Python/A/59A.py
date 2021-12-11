a = str(input())

count_all = sum(1 for i in a)
count_upper = sum(1 for c in a if c.isupper())
count_lower = count_all-count_upper

if count_upper > count_lower:
    print(a.upper())

else:
    print(a.lower())
