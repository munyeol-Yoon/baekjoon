# 제로

# k 개의 줄에 정수 1개 씩
# 정수가 0 인 경우 최근에 쓴 수를 지운다.

k = int(input())

list = []

result = 0

for i in range(k):
    insert = int(input())
    if insert == 0:
        list.pop(len(list) - 1)
    else:
        list.append(insert)

print(sum(list))