# 수학은 비대면 강의입니다

a, b, c, d, e, f = map(int, input().split())

# ax + by = c
# dx + ey = f

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
            print(i, j)
            break