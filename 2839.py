# 설탕 배달

n = int(input())

result = 0 # 결과값 저장할 result 선언

if n % 5 == 0: # 5로 나누어 떨어진다면 결과를 바로저장 후 출력
    result = n // 5
else: # 5로 나누어 떨어지지 않을때
    while True:
        a = 3 # 반복문이 실행될 때마다 n 에 3을 빼주고 result 에 1 을 추가해준다.
        result += 1
        n -= 3
        if n % 5 == 0: # 뺀 값이 5와 나누어떨어진다면 나눈 몫을 result 에 더해주고 반복문 종료
            result = result + n // 5
            break
        elif n == 1 or n == 2: # n 이 5 나 3으로도 나누어지지 않을때 result 에 -1 을 저장하고 종료
            result = -1 
            break
    
print(result)