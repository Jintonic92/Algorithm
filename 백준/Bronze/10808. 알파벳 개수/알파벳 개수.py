word = input()
bin = [ 0 for _ in range(27)]
for each in word:
  #print(each, ord(each))
  bin[ord(each) - 96] += 1
print(*bin[1:27])