#https://codeforces.com/problemset/problem/228/A

shoe = list(map(int ,  input().split(" ")))
answer = 4 - len(set(shoe))
print(answer)