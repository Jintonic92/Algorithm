# input
num_com = int(input())
num_lie = int(input())
graph = [[] for _ in range(num_com+1)]

for i in range(num_lie):
  l, r = map(int, input().split())
  graph[l].append(r)
  graph[r].append(l)

bin = [] # list to count 

def dfs(graph, start, visited):
  visited[start] = True
  bin.append(start)
  for i in graph[start]:
    if visited[i] != True:
      dfs(graph, i, visited)

visited = [0] * (num_com+1)
dfs(graph, 1, visited)

print(len(bin) - 1) # start 하나 빼기 