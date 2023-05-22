s = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    print(s.find(i), end = ' ')

# find 는 해당 값을 찾으면 인덱스의 위치를 반환하고, 해당 인덱스가 없으면 -1을 반환한다. 