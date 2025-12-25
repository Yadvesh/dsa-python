# https://codeforces.com/problemset/problem/96/A

li = list(input())
zero , one = 0,0
for s in li:
    if s == "0":
        zero = zero + 1
        one = 0
        if zero >= 7:
            print("YES")
            exit()
    else:
        one = one + 1
        zero = 0
        if one >= 7:
            print("YES")
            exit()
print("NO")