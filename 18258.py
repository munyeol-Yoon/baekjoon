# 큐 2

# push X  정수 X 를 큐에 넣는다.
# pop  가장 앞에 있는 정수를 뺴고 출력 정수 없을 시 -1
# size 정수 개수 출력
# empty 큐가 비어있으면 1, 아니면 0
# front  큐의 가장 앞에 정수 출력 없으면 -1
# back  큐의 가장 뒤 정수 출력 없으면 -1


#1. 입력 수 받기
#2. 입력 수 만큼 다음 데이터 받기
#3. 큐 생성하기
#4. 각 데이터마다 명령어(push, pop, size, empty, front, back)등을 보면서 해당하는 명령어를 수형
#-> 각 명령어마다 처리해야할 명령어를 정의해서 수행
#5. 수행한 결과를 출력


# 시간 초과 코드
# import sys
# n = int(input())

# q = []

# for i in range(n):
    
#     data = list(map(str,sys.stdin.readline().split()))
    
#     if data[0] == "pop":
#         if len(q) != 0:
#             print(q.pop(0))
#         else:
#             print(-1)
#     if data[0] == "size":
#         print(len(q))
#     if data[0] == "empty":
#         if len(q) == 0:
#             print(1)
#         else:
#             print(0)
#     if data[0] == "front":
#         if len(q) != 0:
#             print(q[0])
#         else:
#             print(-1)
#     if data[0] == "back":
#         if len(q) != 0:
#             print(q[-1])
#         else:
#             print(-1)
#     if data[0] == "push":
#         q.append(data[1])
        


# bool , pop, import sys, heapq , deque, popleft
#pop(index)
#bool(값)

# 명령의 수 N (1 ≤ N ≤ 2,000,000)
# 어지는 정수는 1보다 크거나 같고, 100,000

# 두번쨰 실패 코드 ============= 시간초과
# import sys
# n = int(input())

# q = []

# def pop(q):
#     if len(q) != 0:
#         print(q.pop(0))
#     else:
#         print(-1)

# def size(q):
#     print(len(q))

# def empty(q):
#     print(int(bool(not q)))

# def front(q,n):
#     if len(q) != 0:
#             print(q[n])
#     else:
#         print(-1)

# for i in range(n):
#     data = list(map(str,sys.stdin.readline().split()))
#     if data[0] == "pop":
#         pop(q)
#     if data[0] == "size":
#         size(q)
#     if data[0] == "empty":
#         empty(q)
#     if data[0] == "front":
#         front(q,0)
#     if data[0] == "back":
#         front(q,-1)
#     if data[0] == "push":
#         q.append(data[1])
        
import sys
from collections import deque
n = int(input())

q = deque()


for i in range(n):
    data = list(map(str,sys.stdin.readline().split()))
    #push
    if data[0] == "push":
        q.append(data[1])
    elif data[0] == "pop":
        if len(q)!= 0:
            print(q.popleft())
        else:
            print(-1)
    elif data[0] == "size":
        print(len(q))
    elif data[0] == "empty":
        print(int(bool(not q)))
    elif data[0] == "front":
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif data[0] == "back":
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)