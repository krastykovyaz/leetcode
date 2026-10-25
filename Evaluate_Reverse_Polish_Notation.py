# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Example 1:

# Input: 
tokens = ["1","2","+","3","*","4","-"]

# Output: 5

# Explanation: ((1 + 2) * 3) - 4 = 5


from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    for i in range(len(tokens)):
        if (tokens[i]).isnumeric():
            stack.append(int(tokens[i]))
        elif len(tokens[i]) > 1 and tokens[i][0] == '-':
            stack.append(int(tokens[i]))
        else:
            if tokens[i] == '+':
                count = stack[-1] + stack[-2]
                stack = stack[:-2]
                stack.append(count)
            elif tokens[i] == '*':
                count = stack[-1] * stack[-2]
                stack = stack[:-2]
                stack.append(count)
            elif tokens[i] == '-':
                count = stack[-2] - stack[-1]
                stack = stack[:-2]
                stack.append(count)
            elif tokens[i] == '/':
                count = int(str(stack[-2] / stack[-1] ).split('.')[0])
                stack = stack[:-2]
                # print(count)
                stack.append(count)
    return stack[-1]

if __name__=='__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))