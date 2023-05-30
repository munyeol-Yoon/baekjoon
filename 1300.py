# k 번째 수
n = int(input())
k = int(input())
# 값을 곱했을때 중간값이 양옆의 수랑 본인 값을 더하가너 뺏을때 값이나옴
# 중앙값을 찾는데 이 중앙값이 k 보다 적다.
# 이분 탐색을위한 start, end 를 선언하고, end = k 와 같은값으로 설정한다.
start, end = 0, k # end = 6, 5
res = 0
# start 가 end 와 같거나 적으면 반복, start 가 end와 같아지거나 커지면 반복문 탈출
while start <= end:
    middle = (start + end) // 2 
    # 0 + 7 // 2 = 3 # 중간값 부터 찾기위해 middle 선언 # 1 + 7 // 2 = 4 # 2 + 7 // 2 = 4 # 2 + 6 // 2 = 4 
    # 2 + 5 // 2 = 3
    result = 0 # 결과 값을 저장할 result 선언
    for i in range(1, n+1): # 1 부터 n + 1 만큼 반복
        result = result + min(int(middle / i), n) # 
        # 7
    if result < k:
        start = middle + 1
    else:
        end = middle - 1
        res = middle

print(res)