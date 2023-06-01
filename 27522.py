# 카트라이더

n = 8

score = [10, 8, 6 , 5, 4, 3,2 , 1 ,0]
lst = []
for i in range(n):
    lst.append(input().split())
lst.sort()

red = 0
blue = 0
j = 0
for i in lst:
    if i[1] == 'B':
        blue += int(score[j])
    elif i[1] == 'R':
        red += int(score[j])
    j += 1
if red > blue:
    print('Red')
else:
    print('Blue')

