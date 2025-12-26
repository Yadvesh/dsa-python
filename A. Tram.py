# https://codeforces.com/problemset/problem/116/A

run = int(input())
answer , current_capacity = 0,0
for _ in range(run):
    exit , enter = list(map(int, input().split(" ")))
    current_capacity = current_capacity - exit
    current_capacity = current_capacity + enter
    if current_capacity > answer:
        answer = current_capacity
print(answer)