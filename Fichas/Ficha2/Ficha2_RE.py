import re

#exercício 1
texto = """A 03/01/2022, Pedro viajou para a praia com a sua família.
Eles ficaram hospedados num hotel e aproveitaram o sol e o mar durante toda a semana.
Mais tarde, no dia 12/01/2022, Pedro voltou para casa e começou a trabalhar num novo projeto.
Ele passou muitas horas no escritório, mas finalmente terminou o projeto a 15/01/2022."""

def iso_8601(texto):
    new_texto = re.sub(r'(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/(1[0-9][0-9][0-9]|2[0-9][0-9][0-9])', r'\3-\2-\1', texto)
    return new_texto

print(iso_8601(texto))


#exercicio 2
#txt, png, jpg, docx, 7z
file_names = [
  "document.txt", # válido
  "file name.docx", # inválido
  "image_001.jpg", # válido
  "script.sh.txt", # válido
  "test_file.txt", # válido
  "file_name.", # inválido
  "pasta2", #inválido
  "my_resume.docx", # válido
  ".hidden-file.txt", # válido
  "important-file.text file", # inválido
  "file%name.jpg", # inválido
  "pasta1", #inválido
  "file.7z" # valido
]

def ficheiros(files):
    ficheiro_valido = re.compile(r'^[\w\-\.]+\.(txt|png|jpg|docx|7z)$')
    for file in files:
        if ficheiro_valido.match(file):
            print("É válido")
        else:
            print("É inválido")
        

#exercicio 2.1
def ficheiros2(files):
    ficheiro_valido = re.compile(r'^[\w\-\.]+\.(txt|png|jpg|docx|7z)$')
    extensoes = {}
    for file in files:
        if ficheiro_valido.match(file):
            if ficheiro_valido.match(file).group(1) not in extensoes:
                extensoes[ficheiro_valido.match(file).group(1)] = []
            extensoes[ficheiro_valido.match(file).group(1)].append(file)
    return extensoes


#exercicio 3
lista = [
    "4700-000", # válido
    "9876543", # inválido
    "1234-567", # válido
    "8x41-5a3", # inválido
    "84234-12", # inválido
    "4583--321", # inválido
    "9481-025" # válido
]

def codigos_postais(codigos):
    codigo_valido = re.compile(r'^(\d{4})\-(\d{3})$')
    resultado = []
    for codigo in codigos:
        if codigo_valido.match(codigo):
            resultado.append((codigo_valido.match(codigo).group(1), codigo_valido.match(codigo).group(2)))
    return resultado


#exercicio 4
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
    novo_texto = texto
    for ocorrencia in ocorrencias:
        novo_texto = abreviatura.sub(abrev[ocorrencia], novo_texto, 1)
    return novo_texto


#exercicio 5
matriculas = [
    "AA-AA-AA", # inválida
    "LR-RB-32", # válida
    "1234LX", # inválida
    "PL 22 23", # válida
    "ZZ-99-ZZ", # válida
    "54-tb-34", # inválida
    "12 34 56", # inválida
    "42-HA BQ" # válida, mas inválida com o requisito extra
]

def matricula_valida(matriculas):
    valida = re.compile(r'^\d{2}-[A-Z]{2}-[A-Z]{2}$|'       #11-AA-AA
                        r'^[A-Z]{2}-\d{2}-[A-Z]{2}$|'       #AA-11-AA
                        r'^[A-Z]{2}-[A-Z]{2}-\d{2}$|'       #AA-AA-11
                        r'^[A-Z]{2}-\d{2}-\d{2}$|'          #AA-11-11
                        r'^\d{2}-[A-Z]{2}-\d{2}$|'          #11-AA-11
                        r'^\d{2}-\d{2}-[A-Z]{2}$|'          #11-11-AA

                        r'^\d{2} [A-Z]{2} [A-Z]{2}$|'       #11 AA AA
                        r'^[A-Z]{2} \d{2} [A-Z]{2}$|'       #AA 11 AA
                        r'^[A-Z]{2} [A-Z]{2} \d{2}$|'       #AA AA 11
                        r'^[A-Z]{2} \d{2} \d{2}$|'          #AA 11 11
                        r'^\d{2} [A-Z]{2} \d{2}$|'          #11 AA 11
                        r'^\d{2} \d{2} [A-Z]{2}$'           #11 11 AA
                        )
    for matricula in matriculas:
        if valida.search(matricula):
            print("É válida")
        else:
            print("É inválida")


#exercicio 6
texto = """Num lindo dia de [ESTAÇÃO DO ANO], [NOME DE PESSOA] foi passear com o seu [EXPRESSÃO DE PARENTESCO MASCULINA].
Quando chegaram à [NOME DE LOCAL FEMININO], encontraram um [OBJETO MASCULINO] muito [ADJETIVO MASCULINO].
Ficaram muito confusos, pois não conseguiam identificar a função daquilo.
Seria para [VERBO INFINITIVO]? Tentaram perguntar a [NOME DE PESSOA FAMOSA], que também não sabia.
Desanimados, pegaram no objeto e deixaram-no no [NOME DE LOCAL MASCULINO] mais próximo.
Talvez os [NOME PLURAL MASCULINO] de lá conseguissem encontrar alguma utilidade para aquilo."""

def mad_libs(texto):
    estacao_valida = re.compile(r'^(primavera|verão|outono|inverno)$', re.IGNORECASE)
    pessoa_valida = re.compile(r'^[A-Za-z]+$')
    parentesco_masculino_valido = re.compile(r'^(pai|avô|tio|primo|sobrinho|afilhado|sogro|cunhado|filho|neto|irmão)$', re.IGNORECASE)
    local_feminino_valido = re.compile(r'^[a-z]+a$', re.IGNORECASE)
    objeto_e_adjetivo_e_local_masculino_valido = re.compile(r'^[a-z]+o$', re.IGNORECASE)
    verbo_valido = re.compile(r'^[a-z]+(a|e|i|o|u)r$', re.IGNORECASE)
    nome_plural_masculino_valido = re.compile(r'^[a-z]+os$', re.IGNORECASE)

    print(texto)

    if(re.search(r'\[ESTAÇÃO DO ANO\]', texto)):
        seguinte = False
        while(not(seguinte)):
            estacao = input("Insira a estação do ano: ")
            if (estacao_valida.search(estacao)):
                texto = re.sub(r'\[ESTAÇÃO DO ANO\]', estacao, texto)
                seguinte = True
            else:
                print("Estação inválida")

    if(re.search(r'\[NOME DE PESSOA\]', texto)):
        seguinte = False
        while(not(seguinte)):
            pessoa = input("Insira o nome da pessoa: ")
            if (pessoa_valida.search(pessoa)):
                texto = re.sub(r'\[NOME DE PESSOA\]', pessoa, texto)
                seguinte = True
            else:
                print("Pessoa inválida")

    if(re.search(r'\[EXPRESSÃO DE PARENTESCO MASCULINA\]', texto)):
        seguinte = False
        while(not(seguinte)):
            parentesco_masculino = input("Insira uma expressão de parentesco masculina: ")
            if (parentesco_masculino_valido.search(parentesco_masculino)):
                texto = re.sub(r'\[EXPRESSÃO DE PARENTESCO MASCULINA\]', parentesco_masculino, texto)
                seguinte = True
            else:
                print("Expressão de parentesco masculina inválida")

    if(re.search(r'\[NOME DE LOCAL FEMININO\]', texto)):
        seguinte = False
        while(not(seguinte)):
            local = input("Insira um nome de local feminino: ")
            if (local_feminino_valido.search(local)):
                texto = re.sub(r'\[NOME DE LOCAL FEMININO\]', local, texto)
                seguinte = True
            else:
                print("Local feminino inválido")

    if(re.search(r'\[OBJETO MASCULINO\]', texto)):
        seguinte = False
        while(not(seguinte)):
            objeto = input("Insira um nome de objeto masculino: ")
            if (objeto_e_adjetivo_e_local_masculino_valido.search(objeto)):
                texto = re.sub(r'\[OBJETO MASCULINO\]', objeto, texto)
                seguinte = True
            else:
                print("Objeto masculino inválido")

    if(re.search(r'\[ADJETIVO MASCULINO\]', texto)):
        seguinte = False
        while(not(seguinte)):
            adjetivo = input("Insira um adjetivo masculino: ")
            if (objeto_e_adjetivo_e_local_masculino_valido.search(adjetivo)):
                texto = re.sub(r'\[ADJETIVO MASCULINO\]', adjetivo, texto)
                seguinte = True
            else:
                print("Adjetivo masculino inválido")

    if(re.search(r'\[VERBO INFINITIVO\]', texto)):
        seguinte = False
        while(not(seguinte)):
            verbo = input("Insira um verbo no infinitivo: ")
            if (verbo_valido.search(verbo)):
                texto = re.sub(r'\[VERBO INFINITIVO\]', verbo, texto)
                seguinte = True
            else:
                print("Verbo no infinitivo inválido")

    if(re.search(r'\[NOME DE PESSOA FAMOSA\]', texto)):
        seguinte = False
        while(not(seguinte)):
            pessoa = input("Insira o nome de uma pessoa famosa: ")
            if (pessoa_valida.search(pessoa)):
                texto = re.sub(r'\[NOME DE PESSOA FAMOSA\]', pessoa, texto)
                seguinte = True
            else:
                print("Nome de pessoa famosa inválido")

    if(re.search(r'\[NOME DE LOCAL MASCULINO\]', texto)):
        seguinte = False
        while(not(seguinte)):
            local = input("Insira o nome de um local masculino: ")
            if (objeto_e_adjetivo_e_local_masculino_valido.search(local)):
                texto = re.sub(r'\[NOME DE LOCAL MASCULINO\]', local, texto)
                seguinte = True
            else:
                print("Nome de local masculino inválido")

    if(re.search(r'\[NOME PLURAL MASCULINO\]', texto)):
        seguinte = False
        while(not(seguinte)):
            plural = input("Insira um nome plural masculino: ")
            if (nome_plural_masculino_valido.search(plural)):
                texto = re.sub(r'\[NOME PLURAL MASCULINO\]', plural, texto)
                seguinte = True
            else:
                print("Nome plural masculino inválido")

    print(texto)


#exercício 7
html_file = open("Ficha2.html", "r")

html = html_file.read()

products_dict = {}

produtos = re.findall(r'<div class="product">(.*?)</div>', html, re.DOTALL)

titulo_re = re.compile(r'<h2>(.+)</h2>')
preco_re = re.compile(r'<span class="price">(.+)</span>')
imagem_link_re = re.compile(r'<img src="(.+?)"')
pagina_link_re = re.compile(r'<a class="product-link" href="(.+)"')
caracteristicas_re = re.compile(r'<ul class="features">(.+?)</ul>', re.DOTALL)  #leva '?'
caracteristica_re = re.compile(r'<li>(.+)</li>')

for produto in produtos:
    produto_descricao = []

    titulo = titulo_re.search(produto).group(1)
    preco = preco_re.search(produto).group(1)
    imagem_link = imagem_link_re.search(produto).group(1)
    pagina_link = pagina_link_re.search(produto).group(1)
    caracteristicas_juntas = caracteristicas_re.search(produto).group(1)
    caracteristicas_separadas = caracteristica_re.findall(caracteristicas_juntas)

    produto_descricao.append(("💲 Preço", preco))
    produto_descricao.append(("🖼️ Imagem", imagem_link))
    produto_descricao.append(("🔗 Link", pagina_link))
    produto_descricao.append(("📋 Caraterísticas", caracteristicas_separadas))

    products_dict[titulo] = produto_descricao

print("=== 📦 Produtos Extraídos ===")
for titulo, produto in products_dict.items():
    print("--------------------------------------------------")
    print(f"🛒 Produto: {titulo}")
    for categoria in produto:
        if categoria[0] == "📋 Caraterísticas":
            print(f"{categoria[0]}:")
            for caracteristica in categoria[1]:
                print(f"    - {caracteristica}")
        else:
            print(f"{categoria[0]}: {categoria[1]}")