word = input()
a_list = []
for i in range(1, len(word)-2):
  for j in range(i+1, len(word)):
    a, b, c = word[:i], word[i:j], word[j:]

    a, b, c = a[::-1], b[::-1], c[::-1]
    a_list.append(a+b+c)

print(min(a_list))