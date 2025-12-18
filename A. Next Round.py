#https://codeforces.com/problemset/problem/158/A

contestant = input().split(" ")
score = input().split(" ")
solution = 0;
for i in range(int(contestant[0])):
    if (int(score[i]) > 0 and int(score[i]) >= int(score[int(contestant[1]) - 1])):
        solution += 1
print(solution)