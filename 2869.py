# 달팽이는 올라가고 싶다
# 실패 제한 시간 초과
# a, b, v = map(int, input().split())
# print(a, b, v)

# move = [a, b]

# snail = 0

# result = 0

# while True:
#     result += 1
#     snail += move[0]
#     if snail >= v:
#         break
#     snail -= move[1]
    
# print(result)

import math

a, b, v = map(int, input().split())
print(v - b) # 높이 - 미끄러짐
print(a - b) # 아침이동 - 미끄러짐 = 하루 마다 이동할 수 있는 수
k = (v - b) / (a - b) # 높이 - 미끄러짐 / 아침이동 - 미끄러짐
print(math.ceil(k)) # 목적지에 도달하면 미끄러지지 않기때문에 math.ceil 을 이용해 올림 처리