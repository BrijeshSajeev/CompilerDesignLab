import ply.lex as lex 
 
tokens = ( 
    'IMPORTS', 
    'STRING', 
    'KEYWORD', 
    'FUNCTION', 
    'FLOAT', 
    'INT', 
    'OPERATOR', 
    'ID', 
    'LPARAN', 
    'RPARAN', 
    'SEPRATOR', 
    'LBRACE', 
    'RBRACE', 
) 
 
t_IMPORTS = r'<stdio.h>|<conio.h>|<stdlib.h>' 
t_STRING = r'\".*\"' 
t_KEYWORD = r'\#include|if|else|for|break|int|float|void|String|char|double|while|do' 
t_FUNCTION = r'printf|scanf|clrscr|getch' 
t_FLOAT = r'\d+\.\d+' 
t_INT = r'\d+' 
t_OPERATOR = r'\+|-|\*|/|=|==|<|>|>=|<=' 
t_ID = r'[a-zA-z_][a-zA-Z0-9_]*'  
t_LPARAN = r'\(' 
t_RPARAN = r'\)' 
t_SEPRATOR = r'[;:,]' 
t_LBRACE = r'\{' 
t_RBRACE = r'\}' 
t_ignore = r' |\t' 
 
def t_NEWLINE(t): 
    r'\n+' 
    # t.lexer.lineno += len(t.value) 
 
def t_error(t): 
    print("Illegal character '%s'" % t.value[0]) 
    t.lexer.skip(1) 
 
lexer = lex.lex() 
 
code = open('C:\\Users\\Brijesh\\Desktop\\CD\\EX01A\\text.cpp').read() 
 
lexer.input(code) 
 
while True: 
    tok = lexer.token() 
    if not tok: 
        break 
    print(tok)