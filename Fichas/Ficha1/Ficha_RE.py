import re

#exercicio 0
r'^[01]*$'  #todas as strings binárias
r'^[01]+$'  #todas as strings binárias exceto a string vazia
r'^1[01]*1$' #Todas as strings binárias que começam e terminam por '1'
r'^[01]*00$' #Todas as strings binárias que terminam por "00"
r'^0*(10*){3,}$' #Todas as strings binárias que contêm pelo menos 3 '1'
r'^[01]*110[01]*$' #Todas as strings binárias que contêm a substring "110"
r'^$' #Todas as strings binárias que não contêm a substring "110"????
r'^[01]{2}0[01]*$' #Todas as strings binárias que contêm pelo menos três carateres e o terceiro é '0'
r'^(0|1)[01]*\1$' #Todas as strings binárias que começam e acabam pelo mesmo dígito

#exercicio 1.1
lines = ["hello world", "goodbye world", "hi, hello there"]
def hello():
   for line in lines:
      if re.match(r'hello', line):
        print(f"Deu match na frase: {line}")
      else:
        print(f"Não deu match na frase: {line}")
      
#exercicio 1.2
lines = ["hello world", "goodbye world", "hi, hello there"]
def hello2():
  for line in lines:
    if re.search(r'hello', line):
      print(f"Contém 'hello' na linha. {re.search(r'hello', line)}")
    else:
      print(f"Não contém 'hello' na linha. {re.search(r'hello', line)}")

#exercicio 1.3
line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
def hello3():
  # ocorrencias = re.findall(r'[Hh][Ee][Ll][Ll][Oo]', line)
  ocorrencias = re.findall(r'hello', line, re.IGNORECASE)
  print(ocorrencias)

#exercicio 1.4
line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
def hello4():
  new_line = re.sub(r'hello', "*YEP*", line, flags=re.IGNORECASE)
  print(new_line)

#exercicio 1.5
line = "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."
def virgula():
  elementos = re.split(r',', line)
  print(elementos)

#exercicio 2
def palavra_magica(frase):
  if re.search(r'por favor[!?.]$', frase):
    return ("A frase termina com 'por favor' seguido de um sinal de pontuação")
  else:
    return ("A frase não termina com 'por favor' seguido de um sinal de pontuação")

print(palavra_magica("Posso ir à casa de banho, por favor?"))
print(palavra_magica("Preciso de um favor."))

#exercicio 3
def narcissismo(linha):
    elementos = re.findall(r'\beu\b', linha, re.IGNORECASE)
    return len(elementos)

print(narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."))

#exercicio 4
def troca_de_curso(linha, novo_curso):
    nova_linha = re.sub(r"LEI", novo_curso, linha)
    return nova_linha

fonte = "LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei."
curso = input("Novo curso? ")
print(troca_de_curso(fonte, curso))

#exercicio 5
def soma_string(linha):
    numeros = re.split(r',', linha)
    soma = 0
    for numero in numeros:
        soma += int(numero)
    return soma

print(soma_string("4,10,-6,2,3,8,-3,0,2,-5,1"))
print(soma_string("4,5,-3"))

#exercicio 6
def pronomes(frase):
    pronomes = re.findall(r'\b(eu|tu|ele|ela|nós|vós|eles|elas)\b', frase, re.IGNORECASE)
    return pronomes

print(pronomes("Ola eu vou de certeza. Tu tu e ele, vêm? Eu não espero por vós. Eu estou com pressa, ele tem de vir!"))

#exercicio 7
def variavel_valida(id):
    return bool(re.match(r'[a-zA-Z][\w]*$', id))

print(variavel_valida("aa11_aaaa"))

#exercicio 8
def extrai_inteiros(texto):
    numeros = re.findall(r'[+-]?\d+(?:\.\d+)?', texto)
    return numeros

print(extrai_inteiros(fonte))

#exercicio 9
def underscores( frase ):
    nova_frase = re.sub(r' +', "_", frase)
    return nova_frase

print(underscores("Aqui temos   um belo  exemplo   de frase!"))

#exercicio 10
lista = [
  "4700-000",
  "1234-567",
  "8541-543",
  "4123-974",
  "9481-025",
  "9481-02512",
  "9481-025-123"
]
lista2 = "1100-3#1234-777#1198-999#4715-012"

def codigos(listaCPs):
    resultado = []
    for cp in listaCPs:
      if re.match(r'\d{4}-\d{3}$', cp):
        codigo_par = re.split(r'-', cp)
        resultado.append((codigo_par[0], codigo_par[1]))
    return resultado

print(codigos(lista))
print(codigos(re.split(r'#', lista2)))