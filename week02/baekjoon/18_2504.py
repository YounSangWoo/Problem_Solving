##### 문제 #####
# 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다. 

##### 입력 #####
# 첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.

##### 출력 #####
# 첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다. 

import sys

parenthesis = sys.stdin.readline().rstrip()
print(parenthesis)

stack_A = []
stack_B = []
value = 1
result = 0
paried = True

for i in range(len(parenthesis)):
    if parenthesis[i] == '(':
        stack_A.append(parenthesis[i])
        value *= 2
    elif parenthesis[i] == '[':
        stack_B.append(parenthesis[i])
        value *= 3
    elif parenthesis[i] == ')':
        if stack_A:
            if stack_A.pop() == '(':
                result += value
            value //= 2
        else :
            paried = False
            break
    elif parenthesis[i] == ']':
        if stack_B:
            if stack_B.pop() == '[':
                result += value
            value //= 3
        else :
            paried = False
            break

if not stack_A and not stack_B and paried:
    print(result)
else :
    print(0)
