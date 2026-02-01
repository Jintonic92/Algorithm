import math

h, w, n, m = map(int, input().split())
#h, w, n, m = 5, 4, 1, 1

h_max = math.ceil(h/(n+1))
w_max = math.ceil(w/(m+1))

print(h_max * w_max)