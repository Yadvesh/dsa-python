#https://codeforces.com/problemset/problem/118/A

word = input()
word = word.lower()
answer = ""
for i in range(len(word)):
    if(word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u" or word[i] == "y"):
        continue
    answer = answer + "." + word[i]
print(answer)