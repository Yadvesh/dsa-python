#https://codeforces.com/problemset/problem/617/A

distance = int(input())

if distance % 5 == 0:
    print(distance//5)
    exit()
print(distance//5 + 1)