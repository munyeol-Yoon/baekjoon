# 최소 공배수

import math
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    t = math.lcm(a, b)
    print(t)
