# https://codeforces.com/problemset/problem/520/A

length = int(input())

if length < 26:
    print("NO")
    exit()

string = input()
string = string.lower()
string = set(string)

if len(string) < 26:
    print("NO")
else:
    print("YES")
