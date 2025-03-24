import ply.lex as lex

#exercício 1
texto = """
x=a+1
b=2
a = b-1
a*=2
"""

tokens = (
    'NUM',
    'PLUS',
    'MINUS',
    'TIMES',
    'EQUALS',
    'VAR'
)

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VAR(t):
    r'[a-zA-Z]+'
    return t

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_EQUALS = r'='

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    print("Nova Linha")

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' encontrado")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(texto)

while True:
    linha = input()
    if linha.strip().upper() == "STOP":
        break
    lexer.input(linha)
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == 'VAR':
            print(f"Variável '{tok.value}' \n")
        if tok.type == 'NUM':
            print(f"Número '{str(tok.value)}' \n")
        if tok.type == 'PLUS' or tok.type == 'MINUS' or tok.type == 'TIMES':
            print(f"Operador encontrado")


#exercício 2
