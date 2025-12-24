# https://codeforces.com/problemset/problem/791/A

triple , double = list(map(int, input().split(" ")))
year = 0
while double >= triple:
    double = double*2
    triple = triple*3
    year = year + 1
print(year)