# 괄호

# 테스트를 몇 번 할지 입력받는다.
# 반복문을 선언해 괄호를 넣는다.
# 괄호를 저장할 리스트를 만든다.
# 괄호를 입력받는다.
# 괄호를 하나씩 돌기위해 반복문을 선언한다.
# 괄호를 리스트에 넣으며 검증한다.
# 검증 후 괄호가 저장된 리스트가 비어있으면 YES , 아니면 NO 를 출력한다.

T = int(input())

for i in range(T):
    insert = input() # 괄호를 입력받는다.
    stack = [] # 값을 넣어 확인할 스택 리스트
    for j in insert: # 괄호를 하나씩 반복하며 검증한다.
        if j == '(': # ( 인 경우 stack 에 넣는다.
            stack.append(j)
        elif j == ')': # ) 인 경우
            if stack: # stack 에 값이 있으면 pop
                stack.pop()
            else: # stack 에 값이 없으면 NO 를 출력하고 종료한다.
                print('NO')
                break
    else: # 반복문이 정상적으로 종료되었을때
        if stack: # 스택에 값이 있으면 NO 출력
            print('NO')
        else: # 스택에 값이 없으면 YES 출력
            print('YES')
