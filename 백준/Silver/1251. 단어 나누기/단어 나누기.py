w = input()

a_list = []
for i in range(1, len(w)-1):
  for j in range(i+1, len(w)):
      a, b, c = w[:i], w[i:j], w[j:]
      a, b, c = a[::-1], b[::-1], c[::-1]

      a_list.append(a+b+c)

print(min(a_list))