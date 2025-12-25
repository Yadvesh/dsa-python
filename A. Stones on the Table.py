# https://codeforces.com/problemset/problem/266/A

length = int(input())

s = input()
li = list(s)
boolean = True
i = 0
count = 0
while boolean:
    if i < len(li) - 1:
        if li[i] == li[i+1]:
            li.pop(i)
            i = i - 1
            count = count + 1
    else:
        boolean = False
    i = i + 1
print(count)
    