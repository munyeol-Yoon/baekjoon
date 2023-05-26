# 덱

# https://docs.python.org/3/library/collections.html#collections.deque

from collections import deque
import sys

n = int(input())

q= deque()
for i in range(n):
    data = list(sys.stdin.readline().split()) 
    if data[0] == "push_front":
        q.appendleft(data[1]) 
    elif data[0] == 'push_back':
        q.append(data[1])
    elif data[0] == 'pop_front':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif data[0] == 'pop_back':
        if len(q):
            print(q.pop())
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(q))
    elif data[0] == 'empty':
        print(int(bool(not q)))
    elif data[0] == 'front':
        if len(q):  
            print(q[0])
        else:
            print(-1)
    elif data[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)
