w = input()

a_list = []
for i in range(1, len(w)-1):
  for j in range(i+1, len(w)):
      # print(i, j)
      a, b, c = w[:i], w[i:j], w[j:]
      # print(a, b, c)

      reversed = a[::-1] + b[::-1] + c[::-1]

      a_list.append(reversed)

print(min(a_list))
