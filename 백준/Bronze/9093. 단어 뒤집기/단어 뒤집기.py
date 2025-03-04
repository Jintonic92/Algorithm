import sys

n = int(input())

for _ in range(n):
  sentence = input()
  bin = []
  #sentence = "I am happy today"
  for each in sentence.split():
    bin.append(each)
    bin.append(" ")
  for i in range(len(bin)):
    if bin[i] == "":
      print(" ", end ="")
    else:
      for j in range(len(bin[i])-1, -1, -1):
        print(bin[i][j], end= "")

