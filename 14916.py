# # 거스름돈
# # 처음 작성한 코드
# n = int(input())
# coin = [5, 2]

# count = 0

# while True:
#     if n % coin[0] == 0: # 5의 배수인 경우
#         count = count + n // coin[0]
#         break
#     else: # 5의 배수가 아니면 2백원씩 뺍니다.
#         n -= coin[1]
#         count += 1
#     if n < 0:
#         break

# if n < 0:
#     print(-1)
# else:
#     print(count)

# 두번째로 작성한 코드 

n = int(input())

coin = [5, 2]

count = 0

while n % coin[0] != 0:
    n -= coin[1]
    count += 1
    if n < 0:
        break
if n < 0:
    print(-1)
else:
    count = count + n // coin[0]
    print(count)


# # 모세님 코드

# n = int(input())

# max_num5 = n%5 

# if n == 1 or n == 3: 
#     print(-1)
# elif max_num5%2 == 0:   
#     print((n//5) + max_num5//2)
# else:
#     print((n//5)-1 +(max_num5+5)//2)
