import re
import sys
import math

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def round_ans(left, op, right):
    if op == '*':
        ans = int(left)*int(right)
    if op == '/':
        ans = int(left)/int(right)
    if op == '+':
        ans = int(left)+int(right)
    if op == '-':
        ans = int(left)-int(right)
    return round_half_up(ans, 2)


OPERATOR_MAP = {'*':'/', '/':'*', '+':'-', '-':'+'}
for i, line in enumerate(sys.stdin, start=1):
    line = line.strip()
    left, right = line.split("=")
    if any([operator in right for operator in OPERATOR_MAP]):
        left, right = right, left
    if 'x' in right:
        leftleft, operator, leftright = re.split(r'(?<=[+\-/*])|(?=[+\-/*])', left)
        ans = round_ans(leftleft, operator, leftright)
        print('{0:.2f}'.format(ans))
        continue
    else:
        leftleft, operator, leftright = re.split(r'(?<=[+\-/*])|(?=[+\-/*])', left)
        if leftleft == 'x':
            operator = OPERATOR_MAP[operator]
            ans = round_ans(right, operator, leftright)
            print('{0:.2f}'.format(ans))
            continue
        if leftright == 'x':
            if operator == '-':
                ans = round_ans(leftleft, operator, right)
            elif operator == '+':
                ans = round_ans(right, '-', leftleft)
            elif(operator) == '/':
                ans = round_ans(leftleft, operator, right)
            else:
                ans = round_ans(right, '/', leftleft)
            print('{0:.2f}'.format(ans))