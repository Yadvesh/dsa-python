# https://codeforces.com/problemset/problem/266/B?locale=en

data = list(map(int, input().split(" ")))
queue = list(input())
j = 0
while j < data[1]:
    b = []
    for i in range(data[0] -1):
        if queue[i] == "B" and queue[i+1] == "G":
            b.append(i)
    for x in range(len(b)):
        y = b[x]
        queue[y] = "G"
        queue[y+1] = "B"
    
    j += 1

print("".join(queue))   

