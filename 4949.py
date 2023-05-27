# 균형잡힌 세상

# 1. 문자열 입력받기
# 2. 괄호만 리스트에 넣는다.
# 3. 반복문을 통해 검증한다.
# 4. 출력한다.

# ((((
import sys
while True:
    s = sys.stdin.readline().rstrip()

    stack = []

    # 스택이 비어있으면 yes 아니면 no
    # ([)] 입력시
    # stack = ["(", "["]
    # ["(", "[", ]
    # []()
    # stack = ["[", ""]
    # 
    if s == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ']':
            # 스택이 비어있지 않고 마지막 값이 [ 일때 빼고
            if stack and stack[-1] == '[':
                stack.pop()
            # 스택이 비어있고 마지막 값이 ] 일때 넣기
            else:
                stack.append(i)
        elif i == ')':
            # 스택이 비어있지 않고 마지막 값이 ( 일때 빼고
            if stack and stack[-1] == '(':
                stack.pop()
            # 스택이 비어있고 마지막 값이 ] 일때 넣고
            else:
                stack.append(i)
        else:
            continue

    if not stack:
        print('yes')
    else:
        print('no')

# 민승님 코드 =======================
# while True:
#     stack = []
#     괄호_dict = {
#         ')' : '(',
#         ']' : '[',
#     }
#     success = True
#     string = input()
#     if string == ".":
#         break
#     for str in string:
#         if str in 괄호_dict:
#             if stack and stack[-1] == 괄호_dict[str]:
#                 stack.pop()
#             else:
#                 print('no')
#                 break
#         elif str == '(' or str == '[':
#             stack.append(str)
#     else:
#         if stack:
#             print('no')
#         else:
#             print('yes')

# 시간,  메모리 가장 효과적인 코드
# import sys

# while True:

#     line = sys.stdin.readline().rstrip()

#     if line == '.':
#         break

#     # 스택 생성
#     stack = []

#     # {닫는괄호 : 여는괄호} 형식으로 사전 생성
#     dict = {')' : '(', ']' : '['}

#     # 결과
#     result = "yes"

#     # 문자 검색
#     for char in line:

#         # 열린 괄호라면
#         if char in '([':
#             # 스택에 추가
#             stack.append(char)

#         # 닫힌 괄호라면
#         if char in ')]':

#             # 스택에 열린 괄호가 없다면
#             if (len(stack) == 0):
#                 result = "no"
#                 break

#             else:
#                 # 스택의 TOP과 짝이 맞지 않는다면
#                 if (dict[char] != stack.pop()):
#                     result = "no"
#                     break

#     # 스택에 열린 괄호가 남아있다면
#     if (len(stack) > 0):
#         print("no")
#     else:
#         print(result)