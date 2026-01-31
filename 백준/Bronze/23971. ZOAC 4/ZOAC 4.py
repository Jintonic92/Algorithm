# height width n m 

import sys
import math 

def solution():
    h, w, n, m = map(int, sys.stdin.readline().split())
    
    row_cnt = math.ceil(h/(n + 1))
    col_cnt = math.ceil(w/(m + 1))
    
    print(row_cnt * col_cnt)
    

solution()
            