# https://codeforces.com/problemset/problem/208/A

s = input().strip()

parts = s.split("WUB")

word = []

for p in parts:
    if p:
        word.append(p)
print(" ".join(word))

