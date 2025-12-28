# Contest

run = int(input())

for _ in range(run):
    s = list(input())
    length = len(s) - 1
    condition = True
    i = 0
    while condition:
        
        if s[i] == s[i+1]:
            if s[i] == "Y":
                i = i + 1
            else:
                s.pop(i)
                s.pop(i)
                s.insert(i, "N")
                length = length -1 
                i = 0
        else:
            s.pop(i)
            s.pop(i)
            s.insert(i, "Y")
            length = length -1 
            i = 0
        if "N" not in s:
            condition = False
        if i >= length :
            condition = False
    if len(s) > 1:
        print("NO")
    else:
        print("YES")

