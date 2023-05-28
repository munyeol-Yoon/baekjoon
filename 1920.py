# 수 찾기
# hello 갑시다아
# hello 굿굿

#알고리즘
# 1. n을 입력받는다.
n = int(input())
# 2. A 를 리스트 형태로 n 만큼 입력받는다.
A = list(map(int, input().split()))
# 3. m 을 입력받는다.
m = int(input())
# 4. B 를 리스트 형태로 m 만큼 입력받는다.
B = list(map(int, input().split()))
# 5. A 를 sort 로 정렬한다
A.sort()
# 6. for 문 선언해 인덱스 값을 확인한다.
answer = []
for b in B:
    start,end = 0,n-1
    # while 문 선언 start 와 end 변수를 이용해 탐색을 구현
    while start <= end:
        # 7. n 의 중간값을 찾고, middle 이란 변수에 저장한다.
        middle = (start + end) // 2
        # 찾고자 하는 b 의 값이 A[middle] 과 같다면 answer 리스트에 추가하고 break 를 통해 while 문을 탈출한다.
        if A[middle] == b:
            answer.append(1)
            break
        # 8. 찾고자 하는 b의 값이 middle 보다 적다면 앞의수를 확인한다.
        elif A[middle] > b:
            end = middle - 1
        # 9. 찾고자 하는 m의 값이 middle 보다 크다면 뒤의수를 확인한다.
        else:
            start = middle + 1
    else: # 찾고자 하는 값이 없다면 0 을 추가한다
        answer.append(0)
# 출력한다.
for ans in answer:
    print(ans)


