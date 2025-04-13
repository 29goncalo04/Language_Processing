import ply.lex as lex

#exercício 1
texto = """
x=a+1
b=2
a = b-1
a*=2
b=2<
"""

tokens = (
    'NUMBER',
    'EQUALS',
    'ID',
    'TIMES',
    'PLUS',
    'MINUS'
)

t_EQUALS = r'\='
t_TIMES = r'\*'
t_PLUS = r'\+'
t_MINUS = r'\-'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z]+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    print("Nova linha")

t_ignore = ' \t'

def t_error(t):
    print(f"Caractere inválido: {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(texto)

#caso para testar o 'texto' sem input do stdin
# while True:
#         tok = lexer.token()
#         if not tok:
#             break
#         elif (tok.type == "NUMBER" or tok.type == "ID"):
#             print(f"Variável '{str(tok.value)}'")
#         elif (tok.type == "PLUS" or tok.type == "MINUS" or tok.type == "TIMES"):
#             print(f"Operador encontrado: '{tok.value}'")

while True:
    texto_stdin = input("Introduza texto: ")
    if texto_stdin == "STOP":
        break
    lexer.input(texto_stdin)
    while True:
        tok = lexer.token()
        if not tok:
            break
        elif tok.type == "ID":
            print(f"Variável '{tok.value}'")
        elif tok.type == "NUMBER":
            print(f"Número '{str(tok.value)}'")
        elif (tok.type == "PLUS" or tok.type == "MINUS" or tok.type == "TIMES"):
            print(f"Operador encontrado: '{tok.value}'")


#exercício 2.1
texto = """
@techreport{Camila,
  author ={{projecto Camila}},
  editor ={L.S. Barbosa and J.J. Almeida and J.N. Oliveira and Luís Neves},
  title = "\textsc{Camila} - A Platform for Software Mathematical Development",
  url="http://camila.di.uminho.pt",
  type="(Páginas do projecto)",
  institution = umdi,
  year=1998,
  keyword = "FS",
}
"""

tokens = (
    'LBRACE',
    'RBRACE',
    'COMMA',
    'EQUALS',

    'ATNAME',
    'AUTHOR',
    'EDITOR',
    'TITLE',
    'URL',
    'TYPE',
    'INSTITUTION',
    'YEAR',
    'KEYWORD',

    'STRING'
)

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_EQUALS = r'='

def t_ATNAME(t):
    r'@\w+\{'
    return t

def t_AUTHOR(t):
    r'author'
    return t

def t_EDITOR(t):
    r'editor'
    return t

def t_TITLE(t):
    r'title'
    return t

def t_URL(t):
    r'url'
    return t

def t_TYPE(t):
    r'type'
    return t

def t_INSTITUTION(t):
    r'institution'
    return t

def t_YEAR(t):
    r'year'
    return t

def t_KEYWORD(t):
    r'keyword'
    return t

def t_STRING(t):
    r'(".*?"|\{\{.*?\}\}|\{.*?\}|[a-zA-Z0-9]+)'
    t.value = t.value.strip('"{}') #tira as chavetas e as aspas
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caractere inválido: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(texto)

dados = {}
campo_atual = None
while True:
    tok = lexer.token()
    if not tok:
        break
    elif tok.type == "AUTHOR" or tok.type == "EDITOR" or tok.type == "TITLE" or tok.type == "URL" or tok.type == "TYPE" or tok.type == "INSTITUTION" or tok.type == "YEAR" or tok.type == "KEYWORD":
        campo_atual = tok.type
    elif tok.type == "STRING" and campo_atual:
        dados[campo_atual] = tok.value
        campo_atual = None

print(dados)


#exercicio 3 (?)


#exercicio 4
texto = """
on wc  we 2 + rrv ew 4=off
"""

tokens = (
    'NUMBER',
    'ON',
    'OFF',
    'EQUALS'
)

t_ON = r'(ON|On|oN|on)'
t_OFF = r'(OFF|Off|OFf|OfF|oFf|oFF|ofF|off)'
t_EQUALS = r'='

def t_NUMBER(t):
    r'[+\-]?\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Caractere inválido {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(texto)

pode_somar = False
valor_total = 0

while True:
    texto_stdin = input("Insira texto: ")
    if texto_stdin == "STOP":
        break
    lexer.input(texto_stdin)
    while True:
        tok = lexer.token()
        if not tok:
            break
        else:
            if tok.type == "ON":
                pode_somar = True
            if tok.type == "OFF":
                pode_somar = False
            if tok.type == "NUMBER" and pode_somar == True:
                valor_total += tok.value
            if tok.type == "EQUALS":
                print(valor_total)


#exercicio 5


#exercicio 6