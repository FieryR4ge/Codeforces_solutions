for i in range(int(input())):
    candy = int(input())
    if candy > 2:
        if candy % 2 == 0:
            print(candy//2-1)
        else:
            print(candy//2)
    else:
        print(0)
