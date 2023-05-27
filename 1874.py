# 스택 수열


# 4 일때 ++++-
# 3 일때 -
# 6 일때 ++-
# 8 일때 ++-
# 7 일때 -
# 5 일때 -
# 2 일때 -
# 1 일때 -

# 1. n 을 입력받는다.
# 2. 리스트를 선언한다. 입력값을 저장할 init, 값을 넣을 stack, 결과 +, - 를 넣을 char
# 3. 기준점인 start 변수를 선언한다.
# 4. 반복문을 돌려 입력을 받은 값을 init 에 저장한다.
# 5. init 값을 반복하는 반복문을 선언한다.
# 6. 반복문안에 반복문을 넣는데 기준점은 start 부터 i의 값 + 1 만큼 반복한다.
# 7. 반복하며 1 부터 값을 넣는데 char 에 + 추가, start 도 1 씩 올려준다.
# 8. 바깓쪽 반복문에 if 문을 적는데 스택의 끝에 있는 값이 init 의 값과 같아진다면 stack 을 pop 하고 char 에 - 를 추가한다.
# 9. 그외에는 No 를 출력하고 종료한다.

# n = int(input())
# init = []
# stack = []
# char = []
# start = 1
# # 1 2 3 4 5 6 7 8
# for i in range(n):
#     init.append(int(input()))
# print(init)
# for i in init: # i = 4
#     print(stack)
#     for j in range(start, i+1): # j = 1
#         stack.append(j)
#         char.append('+')
#         start += 1
#     if stack[-1] == i:
#         stack.pop()
#         char.append('-')
#     else:
#         print('No')
#         break
# print(stack)
# print(char)
    


    

n = int(input())
start = 1
stack = []
init = []
char = []

for i in range(n):
    init.append(int(input()))

for i in init:
    for j in range(start, i + 1):
        stack.append(j)
        char.append('+')
        start += 1
    if stack[-1] == i:
        stack.pop()
        char.append('-')
    else:
        char = []
        print('NO')
        break
if char:
    for i in char: 
        print(i)