# https://codeforces.com/problemset/problem/141/A

name1 = input()
name2 = input()

names = name1 + name2
d1 = {}
for ch in names:
    if ch in d1:
        d1[ch] = d1[ch] + 1
    else:
        d1[ch] = 1

mix = input()
d2 = {}
for x in mix:
    if x in d2:
        d2[x] = d2[x] + 1
    else:
        d2[x] = 1

if d1 == d2:
    print("YES")
else:
    print("NO")

