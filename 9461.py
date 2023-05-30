# 파도반 수열

import sys

T = int(sys.stdin.readline())

munyeol = [0 for i in range(101)]
munyeol[0] = 1
munyeol[1] = 1
munyeol[2] = 1

for i in range(T):
    num = int(sys.stdin.readline())
    for i in range(3, num + 1):
        munyeol[i] = munyeol[i -2] + munyeol[i - 3]
    print(munyeol[num - 1])