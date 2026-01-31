# 1 
# +6 7  <- 6 * 1 
# +12 19 < 6 * 2 + * 1 = 6 * 3 + 1
# +18 37 <- 6 * 3 + *2 + * 1 = 6 * 6 + 1
# +24 61 <- 6 * 4 + 6 * 3 + 6 * 2 + 6 * 1 = 6 * 10 + 1

n = int(input())

layer = 1
current_max = 1

while current_max < n:
    current_max += layer * 6
    layer += 1

print(layer)
