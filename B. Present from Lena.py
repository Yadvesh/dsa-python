# https://codeforces.com/problemset/problem/118/B

n = int(input())
lines = []

for k in range(n + 1):
    parts = list(range(k + 1)) + list(range(k - 1, -1, -1))
    line = " ".join(map(str, parts))
    lines.append(" " * (2 * (n - k)) + line)

for line in lines:
    print(line)
for line in reversed(lines[:-1]):
    print(line)
