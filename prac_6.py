#A program to evaluate a postfix expression using a stack.

def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack.pop()

#expr = "23*54*+9-"

expr = input("Enter a postfix expression: ")
result = evaluate_postfix(expr)
print(f"The result of the postfix expression '{expr}' is: {result}") 

