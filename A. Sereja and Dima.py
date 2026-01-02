# https://codeforces.com/problemset/problem/381/A

run = int(input())

sereja, dima = 0 , 0

li = list(map(int , input().split()))

for i in range(run):
    if li[-1] > li[0]:
        if i % 2 == 0:
            sereja += li[-1]
            li.pop(len(li) - 1)
        else:   
            dima += li[-1]
            li.pop(len(li) - 1)
    else:
        if i % 2 == 0:
            sereja += li[0]
            li.pop(0)
        else:   
            dima += li[0]
            li.pop(0)
print( str(sereja) + " " + str(dima))   