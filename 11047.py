# 동전 0

n, k = map(int, input().split())

coin = []

for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

count = 0
for i in coin:
    count = count + k // i 
    # k = 4200 , i = 5000 일땐 몫이 없기떄문에 0 이들어감
    # k = 4200 , i = 1000 일때 나눈 몫 4 를 count 에 더해준다.
    k = k % i
    # k = 4200 , i = 5000 일때 나머지 가 성립이 안되므로 k 의 값은 변화없음
    # k = 4200 , i = 1000 일때 나머지는 200 이므로 200 이 들어감

print(count)