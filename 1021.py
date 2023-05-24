# 회전하는 큐
# 큐의 크기 N
# 뽑아내려는 수 M
# M 은 N 보다 작거나 같은 자연수이다. 
# 양방향 순환 큐를 가지고 있음
# 이 큐에서 몇개의 원소를 뽑아낸다.

'''
q = {1,2,3,4,5,6,7,8,9,10}
뽑을 숫자 : 1, 2, 3
1번 연산을 3번 하면 된다.

q = {1,2,3,4,5,6,7,8,9,10}
뽑을 숫자 : 2, 9, 5
count : 2번과 3번 연산 누적횟수
q = {2,3,4,5,6,7,8,9,10, 1}
count = 1
q = {3,4,5,6,7,8,9,10, 1,}
2를 뽑는다.
count = 1
'''


# 1. n과 m 을 입력받는다.
# 2. 뽑을 숫자를 입력받는다.
# 3. deque 를 만들고 count 를 만든다.
# 4. 반복문안에서 1번 조건이 맞는지 확인한다. ( 1번 조건일 경우 0 )
# 5. 1번 조건이 아닌경우 2번 조건이 맞는지 확인한다.
# 6. 1번 조건이 아닌경우 3번 조건이 맞는지 확인한다.
# 7. count 를 출력한다.



from collections import deque

n, m = map(int, input().split())
select = list(map(int, input().split()))

dq = deque()

for i in range(1, n+1):
    dq.append(i)

count = 0

# 2번 3번을 rotate 를 활용하는건 어떨까
# rotate 는 양수면 오른쪽회전 음수면 왼쪽회전

for i in select: # select 에 들어있는 값만큼 반복
    while True:    
        if dq[0] == i: # dq 의 첫번째 값과 뽑으려는 값이 같으면  첫번째 값을 제거하고 다음 select 값으로 넘어감
            dq.popleft() # 1번 조건 맨 앞의 값을 제거
            break
        else: # 1번 조건이 아닌경우
            if dq.index(i) <= len(dq) / 2: 
                # 뽑고자 하는 인덱스가 덱의 크기의 절반보다 적다면
                # 뒤쪽부터 뽑아낸다.
                # 왼쪽회전 >> 2번 조건
                dq.rotate(-1)
                count += 1
            else:
                # 뽑고자 하는 인덱스가 덱의 크기의 절반보다 크다면
                # 앞쪽부터 뽑아낸다.
                # 오른쪽 회전 >> 3번 조건
                dq.rotate(1)
                count += 1
        
print(count)
    

