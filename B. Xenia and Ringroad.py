# https://codeforces.com/problemset/problem/339/B

houses, task = list(map(int,input().split(" ")))

stops = list(map(int,input().split(" ")))

time = 0

time = stops[0] - 1

for i in range(task -1):   
    if stops[i] > stops[i+1]:
        time = time + (houses - stops[i]) + 1
        time = time + stops[i+1] - 1
    else:
        time = time + stops[i+1] - stops[i]
print(time)