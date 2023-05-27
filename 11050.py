# 이항 계수 1

# n! : factorial = 5 + 4 + 3 + 2 + 1  
import math

n, k = map(int,input().split())

print(math.factorial(n) // (math.factorial(n-k)*math.factorial(k)))