# https://codeforces.com/problemset/problem/110/A

li = list(map(int, input()))
count = 0
for x in li:
    if x == 4 or x == 7:
        count = count + 1
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")