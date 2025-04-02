import re

abreviaturas = {
    "UM": "Universidade do Minho",
    "LEI": "Licenciatura em Engenharia Informática",
    "UC": "Unidade Curricular",
    "PL": "Processamento de Linguagens"
}

texto = "A /abrev{UC} de /abrev{PL} é muito fixe! É uma /abrev{UC} que acrescenta muito ao curso de /abrev{LEI} da /abrev{UM}."

def exercicio4(abrev, texto):
    abreviatura = re.compile(r'/abrev\{([A-Z]+)\}')
    ocorrencias = abreviatura.findall(texto)
    print(ocorrencias)
    novo_texto = texto
    for ocorrencia in ocorrencias:
        novo_texto = abreviatura.sub(abrev[ocorrencia], novo_texto, 1)
    return novo_texto

print(exercicio4(abreviaturas, texto))