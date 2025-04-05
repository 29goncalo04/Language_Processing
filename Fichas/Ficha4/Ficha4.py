import ply.lex as lex
import ply.yacc as yacc

#Exercicios yacc
#  Listas

tokens = ['PA', 'PF', 'VIRG', 'NUM', 'ALFANUM']

t_PA = r'\['
t_PF = r'\]'
t_VIRG = r','
t_NUM = r'\d+'
t_ALFANUM = r'[A-Za-z]\w*'

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


# lista: PA elementos PF
#      | PA PF

#elementos: elementos VIRG elemento
#         | elemento

#elemento: NUM
#        | ALFANUM



def p_lista_elementos(p):
    'lista : PA elementos PF'
    print(f"Lista: {p[1], p[2], p[3]}")
    p[0] = p[2]

def p_lista_PA_PF(p):
    'lista : PA PF'
    print(f"Lista Vazia: {p[1], p[2]}")
    p[0] = 0

def p_elementos_vir(p):
    'elementos : elementos VIRG elemento'
    print(f"Conteúdo da lista: {p[1], p[2], p[3]}")
    p[0] = p[1] + p[3]

def p_elementos_elemento(p):
    'elementos : elemento'
    print(f"Lista com único elemento: {p[1]}")
    p[0] = p[1]

def p_elemento_num(p):
    'elemento : NUM'
    print(f"Elemento numero: {p[1]}")
    p[0] = int(p[1])

def p_elemento_alfanum(p):
    'elemento : ALFANUM'
    print(f"Elemento alfanumerico: {p[1]}")
    p[0] = 0

def p_error(p):
    print(f'Erro na expressão: {p.value}')





parser = yacc.yacc()
resultado  = parser.parse('[78,teste,2]')
print(resultado)






#####################################
#Lista de compras