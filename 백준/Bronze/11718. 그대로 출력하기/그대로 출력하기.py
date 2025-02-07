# sys.stdin.read 
## input은 한줄씩 입력을 받지만, 위 함수는 입력의 끝 EOF End Of File가지 모든 데이터를 한번에 읽어 온다
import sys
input = sys.stdin.read
print(input(), end= "")