# https://codeforces.com/problemset/problem/1236/B

MOD = 10**9 + 7

types_of_presents, guest = map(int, input().split())

choices = (pow(2, guest, MOD) - 1) % MOD
answer = pow(choices, types_of_presents, MOD)

print(answer)
