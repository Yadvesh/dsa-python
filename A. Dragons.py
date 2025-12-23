# https://codeforces.com/problemset/problem/230/A

s , n = list(map(int, input().split(" ")))
d1 = [tuple(map(int,input().split(" "))) for _ in range(n)]
d1.sort()

for i in range(len(d1)):
    if d1[i][0] >= s:
        print("NO")
        exit()
    s = s + d1[i][1]
print("YES")