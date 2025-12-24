# https://codeforces.com/problemset/problem/337/A

students , puzzels = list(map(int, input().split(" ")))
size = list(map(int, input().split(" ")))
size.sort()
boolean = True
i = 0
smallest = 1000
while boolean:           
    if size[i+students -1] - size[i] < smallest:
        smallest = size[i+students -1] - size[i]
    
    if i+students -1 == len(size) - 1:
        boolean = False
        print(smallest)
    i = i + 1