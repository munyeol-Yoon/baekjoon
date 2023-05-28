# 숫자 카드 2

#알고리즘

# 1트 실패=====================
#1. n을 입력받는다
# #1, n만큼 숫자를 입력받아서 A에 저장한다.
# #1. n_list 를 정렬한다.
# n = int(input())
# n_list = list(map(int, input().split()))
# n_list.sort()
# #2. m을 입력받는다
# #2, m만큼 숫자를 입력받아서 B에 저장한다.
# m = int(input())
# m_list = list(map(int, input().split()))
# answer = []
# #2. m_list의 원소들을 꺼내면서 다음과 같은 과정을 수행한다.
# for m_list_index in m_list:
#     #3. cnt 를 0으로 설정한다.
#     cnt = 0
#     #3. start,end을 설정한다. 각각 0, n-1이라고 설정한다.
#     start, end = 0, n - 1
#     #4. start가 end보다 작을때까지 반복한다.
#     while start <= end:
#         #4. (1) middle 를 다음과 같이 설정한다.-> middle = start + end // 2
        
#         middle = (start + end) // 2
#         if n_list[middle] == m_list_index:
#             cnt += 1
#             print(start, end, cnt)
#         elif n_list[middle] < m_list_index:
#             start = middle + 1
#         else:
#             end = middle - 1
#     print(middle)
#     answer.append(cnt)
# print(answer)

# #4. (2) n_list[middle] == B의 각 원소
#     # cnt += 1
# #4. (3) A[middle] < b의 각 원소
#     # start = middle + 1
# #4. (4) A[middle] > b의 각 원소
#     # end = midlle - 1
# #5. while문을 통과하고 cnt를 answer에 추가한다.

# 2트 실패 ============================
# N = int(input())
# N_list = list(map(int, input().split()))
# N_list.sort()
# M = int(input())
# M_list = list(map(int, input().split()))
# index = 0
# answer = {}
# for mIndex in sorted(M_list):
#     cnt = 0
#     while index < len(N_list):
#         if N_list[index] == mIndex:
#             cnt += 1
#             index += 1
#         elif N_list[index] < mIndex:
#             index += 1
#         else:
#             break
#     answer[mIndex] = cnt
# print(' '.join(str(answer[mIndex]) for mIndex in M_list))
# index = 0
#M_list 에 있는 원소들을 하나씩 살피면서 다음과정을 실행한다. 
#1. index < N_list 까지 다음 과정을 반복한다.
#1. (1) cnt = 0으로 초기화를 해준다.
#1, (2) N_list[index] == m : cnt += 1 index += 1
#2. (3) N_list[index] < m : index += 1
#3. (4) N_list[index] > m : break
#4. while 반복문을 나가고 나서 answer에 cnt를 추가해준다.

# [1,2,3,4,5,6,7,8,9,10,11]
# [3,4,5,6,7,8,9,10,10,10,11,12,13]
# {-10: 2, -5: 0, 2: 1, 3: 2, 4: 0, 5: 0, 9: 0, 10: 3}


# 3트 시도 =====================
import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
index = 0
answer = {}
for mIndex in sorted(M_list):
    cnt = 0
    if mIndex not in answer:
        while index < len(N_list):
            if N_list[index] == mIndex:
                cnt += 1
                index += 1
            elif N_list[index] < mIndex:
                index += 1
            else:
                break
        answer[mIndex] = cnt
print(' '.join(str(answer[mIndex]) for mIndex in M_list))

# 다른사람이 Counter 로 푼 코드======================
# import sys
# from collections import Counter

# n = int(sys.stdin.readline())
# cards = Counter(list(map(int, sys.stdin.readline().split())))

# m = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))
# for i in numbers:
#     print(cards[i], end = ' ')