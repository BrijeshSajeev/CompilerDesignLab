import re
patterns =[
    ('FLOAT', r'\d+\.\d+'),
    ('IMPORTS', r'<.*>'),
    ('KEYWORD', r'#include|if|while|for|else|return|break|continue|switch|case|default|do|int|float|double|char|bool|string|void'),
    ('INT', r'\d+'),
    ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('OPERATOR', r'[+\-*/=<>]'),
    ('LPARENTHISIS', r'\('),
    ('RPARENTHISIS', r'\)'),
    ('WHITESPACE', r'\s+'),
    ("STRING",r'\".*\"'),
    ('SEPREATOR',r';|{|}')
]

def lex_tool(source_code):
    tokens = []
    for code in source_code:
        for word in code.split(" "):
           if(word != ' ' and word!= ''):  
                for token_type, pattern in patterns:
                    match = re.match(pattern, word)
                    if match:
                        value = match.group()
                        tokens.append((token_type, value))
                        # source_code = source_code[len(value):]
                        break
                else:
                    raise Exception(f"Invalid character in source code: {word}")
    return tokens
code_txt = open("C:\\Users\\Brijesh\\Desktop\\CD\\EX01A\\text.cpp", "r")
source_code = code_txt.read().split("\n")
# print(source_code)
tokens = lex_tool(source_code)

for token in tokens:
    print(token)