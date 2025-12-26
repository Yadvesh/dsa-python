# https://codeforces.com/problemset/problem/34/A

run = int(input())
li = list(map(int , input().split(" ")))
minimal = 1000
index = 0
for i in range(run):
    if i == run -1:
        diff = abs(li[i] - li[0])
        if diff < minimal:
            minimal = diff
            index = i
    else:
        diff = abs(li[i] - li[i+1])
        if diff < minimal:
            minimal = diff
            index = i
index = index + 1

if index == run:
    print(str(index) + " 1")
else:
    print(str(index) + " " + str(index+1))    