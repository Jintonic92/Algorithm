#n = 3
n = int(input())
bin = []
for _ in range(n):
  bin.append(list(map(int, input().split())))

a = min(row[0] for row in bin)
b = max(row[0] for row in bin)
c = min(row[1] for row in bin)
d = max(row[1] for row in bin)
print((b-a) * (d-c))