# https://codeforces.com/problemset/problem/139/A

target = int(input())
current, index, = 0,0

li = list(map(int,input().split(" ")))

while True:
    current += li[index]
    if current >= target:
        if index == len(li) - 1:
            print("7")
        else:
            print(index + 1)
        break
    index += 1
    if index == len(li) :
        index = 0
        
    