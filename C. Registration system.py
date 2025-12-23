# https://codeforces.com/problemset/problem/4/C

times = int(input())
d1 = {}

for _ in range(times):
    name = input()
    if name in d1:
        d1[name] = d1[name] + 1
        answer = name + str(d1[name])
        print(answer)
    else:
        d1[name] = 0
        print("OK")
