#https://codeforces.com/problemset/problem/231/A

times = int(input())
solution = 0

for _ in range(times):
    votes = list(map(int, input().split()))
    if sum(votes) >= 2:
        solution += 1

print(solution)
