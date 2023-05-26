# 소수 찾기

n = int(input())

arr = list(map(int,input().split()))

count = len(arr)
for i in arr:
    if i == 1:
        count -= 1
    for j in range(2,i):
        if i % j == 0:
            count -= 1
            break

print(count)


# range(2, 2) 면 루프는 0회

# arr = list(map(int,input().split())) 인 경우 len 을 사용할게 아니라면 
# arr = map(int,input().split()) 이렇게 사용할수 있다 이렇게 사용할경우 map 객체 가된다.


'''
[1, 3, 5, 7]
1
count = 4 
i =3 j = 2 
3 % 2 == 0 False
i = 3 j = 3
3 % 3 == 0 True
count -= 1
count = 3

i = 4 j = 2
4 % 2 == 0 True
count -= 1
count = 2
4 % 3 == 0 False
4 % 4 == 0 True
count -= 1
count = 1

i = 5 j = 2
5 % 2 == 0 False
5 % 3 == 0 False
5 % 4 == 0 False
5 % 5 == 0 True
count



'''
