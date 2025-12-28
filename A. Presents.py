# https://codeforces.com/problemset/problem/136/A

length = int(input())

li = list(map(int, input().split(" ")))
answer = [0] * length
final = ""
for i in range(length):
    index = li[i] - 1   
    answer[index] = i + 1
    


for j in range(length):
    final = final +str(answer[j]) + " "  
print(final)