def infix_to_postfix(expression):
    stack = []
    postfix = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for char in expression:
        if char.isalnum():  # If the character is alphanumeric (operand)
            postfix.append(char)  # Append it to the postfix expression
        elif char == '(':  # If the character is an opening parenthesis
            stack.append(char)  # Push it onto the stack
        elif char == ')':  # If the character is a closing parenthesis
            while stack and stack[-1] != '(':  # Pop operators from the stack and append them to the postfix expression
                postfix.append(stack.pop())
            if stack:  # If the stack is not empty (there was a matching opening parenthesis)
                stack.pop()  # Remove the opening parenthesis from the stack
        else:  # If the character is an operator
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:  # Pop operators with higher or equal precedence from the stack and append them to the postfix expression
                postfix.append(stack.pop())
            stack.append(char)  # Push the current operator onto the stack

    while stack:  # Pop any remaining operators from the stack and append them to the postfix expression
        postfix.append(stack.pop())

    return ''.join(postfix)  # Return the postfix expression as a string
 
def create_three_address_code(postfix_expr):
    stack = []
    code = []
    temp_var = 0

    for char in postfix_expr:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            temp_var += 1
            temp_name = f"t{temp_var}"
            code.append(f"{temp_name} = {operand1} {char} {operand2}")
            stack.append(temp_name)

    return code


# expres = '3+4*(8-7*(c-b)+2)'  
expres = 'a+a*(b-c)+d*(b-c)'  
print(create_three_address_code(infix_to_postfix(expres)))
print(infix_to_postfix(expres))