# ATM

N = input()
T = list(map(int, input().split()))
T.sort()
for i in range(1, len(T)):
    T[i] = T[i-1] + T[i]
    
print(sum(T))