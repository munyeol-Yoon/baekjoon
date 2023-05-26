# 요세푸스 문제 0

from collections import deque

n , m = map(int, input().split())

deq = deque([str(i) for i in range(1, n + 1)])
#리스트 내포 
# for i in range(1, n + 1):
#     deq.append(str(i))
# centi_meter_list = [100*i for i in meter_list] 
list = [] 
# <3, 6, 2, 7, 5, 1, 4>
while len(deq) != 0:
    deq.rotate(-(m-1))
    list.append(deq[0])
    deq.popleft()
    
result = ", ".join(list)
print(f"<{result}>")
# 1. n, m 을 입력받는다.
# 2. deque 에 n 만큼 값을 채워 넣는다.
# 3. while 문을 선언해 deque 에 값이 없으면 탈출하게 만든다.
# 4. while 문에서 n 번째 값을 pop 해서 값을 result 에 넣는다.    hint pop은 선언만 되도 된다
# 5. 출력한다.

# [3, 4, 5, 6, 7, 1, 2]
# rotate(3)
# popleft
