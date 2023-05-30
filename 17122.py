# 체스

# 1. 8x8 의 딕셔너리를 만든다.
# 2. 딕셔너리의 키값 A

#2차원 배열 만들자 !!!!

# [[0] * 8] * 8 이렇게 중첩된 배열을 선언할 경우 얕은 복사가 일어나므로 하나만바꿔도 전부다 바꿘디.
# list(n) # ******* 문자열을 리스트로 바꾸면 쉽게 분할할 수 있다.

# 런타임 에러 코드 ============================

# board = [[0 for _ in range(8)] for _ in range(8)] 
# for i in range(8):
#     for j in range(8):
#         if i % 2 == 0 and j % 2 == 0: # i = 0, j = 0,1,2,3,4,5,6,7,8
#             board[i][j] = 1
    
#         elif i % 2 != 0 and j % 2 != 0:  
#             board[i][j] = 1
# alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H']

# 이제부터 0은 검정 1은 흰색
# 


# for _ in range(T):
#     n, m = input().split()
#     alphabet , number = list(n)[0],list(n)[1] 
#     test1 = board[alpha.index(alphabet)][int(number)]

#     몫,나머지 = divmod(int(m),8)
#     if 나머지 == 0:
#         test2 = board[나머지 - 1][몫]
#     else:
#         test2 = board[나머지-1][몫+1]
#     if test1 == test2:
#         print("YES")
#     else:
#         print("NO")
# print(f"T: {T}, N: {n}, M: {m}")



# 2트 틀렸습니다 ==============================

# T = int(input())

# alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# for _ in range(T):
#     n,m = input().split()
#     alphabet , number = list(n)[0],list(n)[1]
#     몫,나머지 = divmod(int(m),8)
#     가로 = alpha[나머지-1]
#     세로 = str(몫 + 1)
#     if ( 가로 and alphabet ) in ['A','C','E','G'] and  (number and 세로) in ['1','3','5','7']:
#         print('YES')
#     elif ( 가로 and alphabet ) in ['B','D','F','H'] and  (number and 세로) in ['2','4','6','8']:
#         print('YES')
#     else:
#         print('NO')

# 3트 가즈아! 3트 실패 코드 if 지옥 정신이 나가버려 포기 ==============================
# 3 17
# 2 9
# 1 1

# A 라고 했을때
# 3 // 17 = 5
# 2 // 9 = 4
# 1 // 1 = 1 홀수는 흑 짝수는 백
# j // list_n[1] = 홀짝
# T = int(input())
# alpha_odd = ['A', 'C', 'E', 'G']
# alpha_even = ['B', 'D', 'F', 'H']
# result = 0
# for _ in range(T):
#     n, m = input().split()
#     list_n = list(n)

#     for j in range(1, 8):
#         if list_n[0] in alpha_odd:
#             if (j // list_n[1]) % 2 == 0:
#                 pass # 여기가 백
#             elif (j // list_n[1]) % 2 != 0:
#                 pass # 여기가 흑
#         elif list_n[0] in alpha_even:
#             if (j // list_n[1]) % 2 == 0:
#                 pass # 여기가 흑
#             elif (j // list_n[1]) % 2 != 0:
#                 pass # 여기가 백


# 4트 가자!! 4트 실패 ================================
# T = int(input())
# alpha = {
#     'A':  0, 
#     'B' : 1,
#     'C' : 2,
#     'D' : 3,
#     'E' : 4,
#     'F' : 5,
#     'G' : 6, 
#     'H' : 7,
# }

# for _ in range(T):
#     n,m = map(str, input().split())
#     몫,나머지 = divmod(int(m),8)
#     가로1,세로1 = alpha[list(n)[0]],int(list(n)[1])
#     if 나머지 == 0:
#         가로2,세로2 = 8,몫+1
#     else:
#         가로2,세로2 = 나머지-1,몫+1
#     if ( 가로1 - 가로2 ) % 2 == 0 and (세로1 - 세로2) % 2 == 0:
#         print('YES')
#     elif 가로1 == 가로2 or 세로1 == 세로2:
#         print('YES')
#     else:
#         print('NO')

# 5  트 가보자아아아ㅏㅏㅏㅏㅏㅏ하아..





# 정답 코드 ==================


board = [[0 for _ in range(8)] for _ in range(8)] 
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0: # i = 0, j = 0,1,2,3,4,5,6,7,8
            board[i][j] = 1
    
        elif i % 2 != 0 and j % 2 != 0:  
            board[i][j] = 1

T = int(input())

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H']

for _ in range(T):
    a,b = input().split()
    al,bl = alpha.index(list(a)[0]),int(list(a)[1])
    test1 = board[bl-1][al]
    몫,나머지 = divmod(int(b),8)
    if 나머지 == 0:
        test2 = board[몫-1][7]
    elif 몫 == 7:
        test2 = board[몫][나머지-1]
    else:
        test2 = board[몫][나머지-1]
    if test1 == test2:
        print("YES")
    else:
        print("NO")
    


# ord 사용 코드 ================ 하 현타...
# t = int(input())

# for _ in range(t):
#     c1, c2 = input().split()
#     x1, y1 = ord(c1[0]) - ord('A'), int(c1[1]) - 1
#     x2, y2 = divmod(int(c2) - 1, 8)

#     if (x1 + y1) % 2 == (x2 + y2) % 2:
#         print("YES")
#     else:
#         print("NO")