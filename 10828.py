# 스택

# 1. n 을 입력 받는다.
# 2. n 만큼 반복해 명령을 입력받는다.
# 3. 명령어를 구분해 입력받는다. (push 1 , pop ...)
# 4. 각 조건에 맞는 명령을 실행한다.
'''
 elif command[0] == 'top':
    if len(stack):
        print(stack[-1])

'''

import sys

n = int(input())

list = []
data = []
for i in range(n):
    list = sys.stdin.readline().split()
        
    if list[0] == "push":
        data.append(list[1])
    elif list[0] == "pop":
        if bool(data):
            print(data.pop())
        else:
            print(-1)
    elif list[0] == "size":
        print(len(data))
    elif list[0] == "empty":
        if bool(data):
            print(0)
        else:
            print(1)
    elif list[0] == "top":
        if bool(data):
            print(data[len(data) -1])
        else:
            print(-1)


import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)

    elif command[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(stack))
    
    elif command[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)