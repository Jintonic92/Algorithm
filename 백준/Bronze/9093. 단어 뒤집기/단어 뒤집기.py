# 9093 단어 뒤집기

n = int(input())
for _ in range(n):
    sent = input()
    bin = []
    
    for each in sent.split():
        bin.append(each)
        bin.append(" ")
        
    for i in range(len(bin)):
        if bin[i] == " ":
            print(" ", end = "")
        else:
            for j in range(len(bin[i])-1, -1, -1):
                print(bin[i][j], end = "")


  

