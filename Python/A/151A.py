n = list(map(int, input().split()))
bottle = n[1] * n[2] // n[6]
lime = n[3] * n[4]
salt = n[5] // n[7]

print(min(bottle, lime, salt)//n[0])
