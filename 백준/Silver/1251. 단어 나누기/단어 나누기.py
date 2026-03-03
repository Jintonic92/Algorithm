word = input()
a_list = []
for i in range(1 ,len(word)-1):
  for j in range(i+1, len(word)):
    a, b, c = word[:i], word[i:j], word[j:]
    
    reversed = a[::-1] + b[::-1] + c[::-1]
    a_list.append(reversed)

print(min(a_list))