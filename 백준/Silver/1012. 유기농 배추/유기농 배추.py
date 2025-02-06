from collections import deque


dx = [1, -1, 0 , 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append([x,y])
  cnt = 1

  while queue:
    x, y = queue.popleft()

    for i in range(len(dx)):
      nx = x + dx[i]
      ny = y + dy[i]


      if 0<= nx < n and 0 <= ny < m:
        if bin[nx][ny] != 0 and not visited[nx][ny] :
          visited[nx][ny] = True
          queue.append([nx, ny])
          cnt += 1
  
  return cnt

test_case = int(input())
for _ in range(test_case):
  n, m, how = map(int, input().split())
  bin = [[0 for _ in range(m)] for _ in range(n)]
  visited = [[0 for _ in range(m)] for _ in range(n)]

  for i in range(how):
    x, y = map(int, input().split())
    bin[x][y] = 1
  
  result = []
  for x in range(n):
    for y in range(m):
      if not visited[x][y] and bin[x][y] == 1:
        each = bfs(x, y)
        result.append(each)

  print(len(result))

  

