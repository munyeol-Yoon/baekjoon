# 피보나치 함수

# before==================================

# zeroCount = 0
# oneCount = 0
# def fibonacci(n):
#     global zeroCount
#     global oneCount
    
#     if n == 0:
#         zeroCount += 1
#         return zeroCount
#     elif n == 1:
#         oneCount += 1
#         return oneCount
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# m = int(input())
# for i in range(m):
#     n = int(input())
#     fibonacci(n)
#     print(zeroCount, oneCount)
#     zeroCount, oneCount = 0, 0

#__________ မင်္ဂလာပါ______밍그라바_______

# 0의 갯수 = 이전 1의 갯수, 1의 갯수 = 이전 0+이전1 갯수
t = int(input())

for _ in range(t):
    zeroCount = [1, 0, 1]
    oneCount = [0, 1, 1]
    n = int(input())
    
    for j in range(3, n + 1):
        oneCount.append(oneCount[j-1] + oneCount[j-2])
        zeroCount.append(zeroCount[j-1] + zeroCount[j-2])
        
    print(zeroCount[n], oneCount[n])




# 0     1 0     
# 1     0 1
# 2     1 1    
# 3     1 2      
# 4     2 3  
# 5     3 4  
# 6     5 7 
# 7     8 13
# 8    13 20
# 9    21 33              