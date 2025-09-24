bin  = []
n = int(input())

for _ in range(n):
    w, h = map(int, input().split())
    bin.append((w, h))

answer = []
for i in range(len(bin)):
    rank = 1
    for j in range(len(bin)):
        if bin[i][0] < bin[j][0] and bin[i][1] < bin[j][1]:
            rank += 1
    answer.append(rank)

for each in answer:
    print(each, sep=" ")