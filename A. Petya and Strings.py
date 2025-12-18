#https://codeforces.com/problemset/problem/112/A

word1 = input()
word2 = input()
word1 = word1.lower()
word2 = word2.lower()
for i in range(len(word1)):
    if(word1[i] > word2[i]):
        print("1")
        exit()
    elif(word1[i] < word2[i]):
        print("-1")
        exit()
print(0)