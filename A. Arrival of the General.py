# https://codeforces.com/problemset/problem/144/A

length = int(input())
li = list(map(int,input().split(" ")))

index_max = 0
index_min = 0
largest = li[0]
smallest = li[-1]

for i in range(length):
    if li[i] > largest:
        largest = li[i]
        index_max = i
    if li[i] <= smallest:
        smallest = li[i]
        index_min = i

if index_max > index_min:
    answer = index_max + ((length - 1) - (index_min + 1))
else:
    answer = index_max + (length -1 - index_min)
print(answer)
