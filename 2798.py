# 블랙잭
n,m = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
munyeol = []
for i in data:
    for j in data:
        if i == j:
            continue
        for k in data:
            if i == k:
                continue
            if j == k:
                continue
            # print("------")
            # print("i:", i ,"j:", j, "k:", k)
            # print(i + j + k)
            sum_num = i + j + k
            if sum_num <= m:
                munyeol.append(sum_num)

print(max(munyeol))

