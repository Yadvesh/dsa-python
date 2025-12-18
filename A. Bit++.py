#https://codeforces.com/problemset/problem/282/A

times = int(input())
answer = 0

for _ in range(times):
    expression = input()
    if(expression[1] == "+"):
        answer = answer + 1
    else:
        answer = answer - 1    
print(answer)