# 분해합
num = int(input())
result = 0
for i in range(num):
    list_1 = list(map(int, str(i))) # [1, 9, 8]
    sum_num = sum(list_1) # 18
    if num == i + sum_num: # i = 198 
        # num = 216 이랑 198 + 18 이 같으면 result 에 저장 하고 반복문 종료
        result = i
        break
print(result)
