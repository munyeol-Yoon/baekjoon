# 소수 구하기

# 시간 초과 발생 

# n, m = map(int, input().split())
# print(n, m)

# # list = []

# # 1. 숫자를 입력 받는다.
# # 2. 숫자가 1 이라면 생략
# # 3. 2 부터 i 가 될때까지 반복해 소수인지 판별한다. 조건문에 만약 나누어지는 숫자라면 반복문을 탈출한다.
# # 4. else 문이 실행되지 않는다.
# # 5. 반복문이 무사히 실행되었을 경우 소수를 출력한다.

# for i in range(n, m + 1):
#     if i == 1:
#         continue
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# # for-else 문은 break 등으로 중간에 빠져나오지 않고 끝까지 실행되었을 경우 else 문이 실행된다.

# # print(list)

# ==========틀렸습니다.

# import math

# n, m = map(int, input().split())

# for i in range(n, m + 1):
#     if i == 1:
#         continue
#     for j in range(2, math.ceil(i**0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)


'''
제곱근을 활용하자
에라토스테네스의 체를 활용해 문제를 푼결과 계속 오류가 났다.
결국 시간 복잡도를 줄여야만 했다.
제곱근을 이용해 연산을 최소화하는 건데 수포자라 잘은모름
대충 설명하자면 제곱과 제곱근을 이용해 약수를 구할 수 있는데 
30의 약수는 1*30 , 2*15, 3*10, 5*6 
그리고 6*5, 10*3, 15*2, 30*1 이기 때문에 역순 관계이다.
즉, 앞에 4개만 찾으면 되고 연선을 절반이나 줄일 수 있어진다.
5는 30의 제곱근 (5.477777777...) 과 비슷하기때문에 
30의 제곱근까지 구한 수에서만 약수를 구하고 나눈 몫을 구한다.

다른 방법으로 math 라이브러리에 sqrt 가 있다.
'''
# 정답
# n, m = map(int, input().split())

# for i in range(n, m + 1):
#     if i == 1:
#         continue
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

#=========== 아래는 math 라이브러리의 sqrt 를 활용한 방법이다.
# 백준 결과를 보니 메모리와 시간이 비슷하다 마음에 드는 걸 활용하면 될듯.

import math

n, m = map(int, input().split())

for i in range(n, m + 1):
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        print(i)