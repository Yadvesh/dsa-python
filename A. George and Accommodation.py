# https://codeforces.com/problemset/problem/467/A

run = int(input())

count = 0

for _ in range(run):
    living , space = list(map(int , input().split(" ")))
    if space - living >=2:
        count += 1
print(count)