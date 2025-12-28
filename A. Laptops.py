# https://codeforces.com/problemset/problem/456/A

laptops = int(input())
data = []

for _ in range(laptops):
    a , b = list(map(int , input().split(" ")))
    data.append((a ,b))
data.sort()

for i in range(len(data)):
    price , quality = data[i]
    for j in range(i+1, len(data),1):
        new_price , new_quality = data[j]
        if new_price > price:
            if new_quality >= quality:
                print("Poor Alex")
                exit()
print("Happy Alex")
