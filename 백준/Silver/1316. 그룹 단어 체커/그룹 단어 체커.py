n = int(input())
count = n

for _ in range(n):
    word = input()
    #print(word)
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            count -= 1
            #print(count, "break")
            break

print(count)