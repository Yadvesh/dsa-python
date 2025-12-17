#https://codeforces.com/problemset/problem/71/A

times = int(input())

for _ in range(times):
    word = str(input())
    if len(word) > 10:
        print(word[0] + str(len(word)-2) + word[-1])
    else:
        print(word)