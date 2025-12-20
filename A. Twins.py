#https://codeforces.com/problemset/problem/160/A

coins = int(input())
values = list(map(int , input().split(" ")))
values.sort(reverse=True)
total, count = 0.0,0
target = sum(values)/2

for i in values:
   total = total + i 
   count = count + 1
   if total > target:
      print(count)
      exit()