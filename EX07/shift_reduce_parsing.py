 
gram = { 
    "S": ["S+S", "S*S",'S-S','(S)', "i"] 
} 

start = "S"
input = "(i+i)$"
stack = '$'
print(f'{"Stack":<15}'+f'{"Input":<15}'+"Parsing Action")
print(f'{"-"*45}')

while True:
    i=0
    for i in range(len(gram[start])):
        if gram[start][i] in stack:
            stack = stack.replace(gram[start][i],start)
            print(f'{stack:<15}{input:<15}'+f'Reduce : {start} -> {gram[start][i]}')
    if len(input) > 1:
        stack +=input[0]
        print(f'{stack:<15}{input:<15}'+f'Shift : {input[0]}')
        input = input[1:]
    if stack == ("$"+start):
        if input == "$":
            print(f'{stack:<15}{input:<15}'+f'Accept!')
            break
        else:
            print(f'{stack:<15}{input:<15}'+f'Reject!')
            exit()