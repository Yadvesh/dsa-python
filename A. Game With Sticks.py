# https://codeforces.com/problemset/problem/451/A

a , b = list(map(int,input().split(" ")))

if min(a,b) % 2 == 0:
    print("Malvika")
else:
    print("Akshat") 