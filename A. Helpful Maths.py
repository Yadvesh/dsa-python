#https://codeforces.com/problemset/problem/339/A

numbers = list(input())

numbers = [x for x in numbers if x != "+"]

numbers.sort()
answer = ""
for i in range(len(numbers)):
    answer = answer + "+" + numbers[i] 
print(answer[1:])