# https://codeforces.com/problemset/problem/474/A

s = "qwertyuiopasdfghjkl;zxcvbnm,./"

direction = input()

if direction == "R":
    value = -1
else:
    value = 1

chars = input()
answer = ""

for i in chars:
    for j in range(len(s)):
        if s[j] == i:
            answer = answer + s[j + value]

print(answer)