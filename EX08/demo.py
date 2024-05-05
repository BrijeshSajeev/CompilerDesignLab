def po_inf(expr):
    PRI ={'+':1,'-':1,'*':2,'/':2}
    stack = []
    postfix=[]
    for i in expr:
        if i.isalnum():
            postfix.append(i)
        elif i =='(':
            stack.append(i)
        elif i==')':
            while stack and stack[-1]!='(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1]!='(' and PRI[i] <= PRI[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(i)
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)
expres = '3+4*(8-7*(c-b)+2)'  
print(po_inf(expres))