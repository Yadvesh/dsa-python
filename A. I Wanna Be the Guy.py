# https://codeforces.com/problemset/problem/469/A

levels = int(input())

levels1 = list(map(int, input().split(" ")))
levels1.pop(0)
levels2 = list(map(int, input().split(" ")))
levels2.pop(0)
total = levels1 + levels2

total =  set(total)

for i in range(levels):
    if i+1 in total:
        pass
    else:
        print("Oh, my keyboard!")
        exit()
print("I become the guy.")