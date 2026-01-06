# https://codeforces.com/problemset/problem/433/B


# Takes very long time to complete

# stones = int(input())

# li = list(map(int, input().split(" ")))
# order = sorted(li)

# run = int(input())
# for _ in range(run):
#    sum = 0
#    type, start, end = list(map(int, input().split(" ")))
#    if type == 1:
#       for i in range(start - 1, end, 1):
#           sum += li[i]
#   else:
#      for j in range(start - 1, end, 1):
#          sum += order[j]
#  print(sum)

# Prefix sums

stones = int(input())
li = list(map(int, input().split(" ")))
order = sorted(li)

prefix_li = [li[0]]
prefix_order = [order[0]]

for i in range(1, stones):
    val = li[i] + prefix_li[i - 1]
    prefix_li.append(val)
    kal = order[i] + prefix_order[i - 1]
    prefix_order.append(kal)

run = int(input())

for j in range(run):
    type, start, end = list(map(int, input().split(" ")))
    if type == 1:
        if start == 1:
            print(prefix_li[end -1])
        else:
            answer = prefix_li[end -1] - prefix_li[start -2]
            print(answer)
    else:
        if start == 1:
            print(prefix_order[end -1])
        else:
            answer = prefix_order[end -1] - prefix_order[start -2]
            print(answer)
    