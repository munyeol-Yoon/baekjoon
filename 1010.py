# 다리 놓기
import math
t = int(input())

for i in range(t):
    count = 1
    west, east = map(int, input().split())
    b = int(math.factorial(east) / (math.factorial(west)*(math.factorial(east-west))))
    print(b)