# 약수

n = int(input())
t = list(map(int, input().split()))

t.sort()

if len(t) % 2 == 0:
    answer = t[0] * t[-1]
else:
    num = len(t) // 2        
    answer = t[num] ** 2
print(answer)

'''
이렇게도 푸네요 ㄷㄷ
n = int(input())
a = list(map(int, input().split()))
a_max = max(a)
a_min = min(a)
print(a_max * a_min)
'''

# 그저 goat, 빛


#천재다 ㄷㄷ....
# a = [1,2,4] => [2]

# len(a)//2
# 홀수 -> index(n) 가운데거 ^ 2
# 짝수 -> sort 해서 맨앞, 맨 뒤 곱하기