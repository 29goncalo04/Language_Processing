import re

#exercicio 4
def troca_de_curso(linha, novo_curso):
    nova_linha = re.sub(r"LEI", novo_curso, linha)
    return nova_linha

fonte = "LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei."
curso = input("Novo curso? ")
print(troca_de_curso(fonte, curso))


#exercicio 5
def soma_string(linha):
    result = re.split(r',', linha)
    soma = 0
    for i in result:
      soma+=int(i)
    return soma

print(soma_string("4,10,-6,2,3,8,-3,0,2,-5,1"))

#exercicio 10
lista = [
    "4700-000",
    "1234-567",
    "8541-543",
    "4123-974",
    "9481-025"
]

lista2 = "1100-3#1234-777#1198-999#4715-012"

def codigos(listaCPs):
  output = []
  for cp in listaCPs:
    if re.match(r'\d{4}-\d{3}', cp):
      output.append(cp)
  return output
  
print(codigos(lista))
print(codigos(re.split(r'#',lista2)))