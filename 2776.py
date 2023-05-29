# 암기왕
t = int(input())

for case_t in range(t):

    n = int(input())
    # n 을 입력받는다.

    n_list = list(map(int, input().split()))
    # n_list 를 입력받는다.
    n_list.sort()
    m = int(input())
    #  m 을 입력받는다.

    m_list = list(map(int, input().split()))
    # m_list 를 입력받는다.

    answer = []
    # 결과값을 저장할 answer 리스트를 만든다.

    for m_index in m_list:
        start, end = 0, n - 1
        # 값을 이분탐색으로 찾기 위한 변수 start 와 end 를 선언한다.
    # for 문으로 m_list 의 값을 하나씩 꺼낸다.
        while start <= end:
        # while 문을 선언하는데 start 와 end 가 같아질때까지 반복한다.
            middle = (start + end) // 2
            # start 와 end 를 2로 나눈값을 가진 middle 변수를 선언한다.
            if m_index == n_list[middle]:
                # if 문으로 찾고자 하는 값이 있다면 리스트에 1을 저장한다.
                answer.append(1)
                break
            elif m_index < n_list[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            # 찾고자하는 값이 없다면 0을 저장한다.
            answer.append(0)

    for ans in answer:
        print(ans)

# 나영님 코드 ============================
# t = int(input())

# for i in range(t):
#     b1 = int(input())
#     book1 = set(map(int,input().split()))         # {1, 2, 3, 4, 5}
#     b2 = int(input())
#     book2 = map(int,input().split())              # [1, 2, 3, 4, 5]
#     for j in book2:
#         if j in book1:
#            print(1)
#         else:
#             print(0)
# # set 중복제거 하고 리스트는 아닌데 