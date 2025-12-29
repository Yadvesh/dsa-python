# https://codeforces.com/problemset/problem/119/A

from math import gcd

simon , antision , stones = list(map(int,input().split(" ")))
boolearn = True
count = 1
while boolearn:
    if count % 2 != 0:
        substract = gcd(simon,stones)
        if substract > stones:
            print("1")
            exit()
        else:
            stones = stones - substract
    else:
        substract = gcd(antision,stones)
        if substract > stones:
            print("0")
            exit()
        else:
            stones = stones - substract
    count = count + 1
    