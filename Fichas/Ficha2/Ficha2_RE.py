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


#exercicio 4 ???????????????????????????????????? (mal feito)
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



#exercício 7
html_file = open("Ficha2.html", "r")

html = html_file.read()

products_dict = {}

products = re.findall(r'<div class="product">(.*?)</div>', html,re.DOTALL)

# Compiling the expressions
title_re = re.compile(r'<h2>(.*)</h2>')
price_re = re.compile(r'<span class="price">(.*)</span>')
image_url_re = re.compile(r'<img src="(.*?)"')
product_url_re = re.compile(r'<a class="product-link" href="(.*)"')
features_re = re.compile(r'<ul class="features">(.*)</ul>',re.DOTALL)
single_feature_re = re.compile(r'<li>(.*)</li>')
for product in products:

    # List with all the product description
    product_description = []

    # Consuming the information
    title = title_re.search(product).group(1)
    price = price_re.search(product).group(1)
    image_url = image_url_re.search(product).group(1)
    product_url = product_url_re.search(product).group(1)
    features = features_re.search(product).group(1)
    features = single_feature_re.findall(features)

    # Adding the information to the product description list
    product_description.append(("💲 Preço", price))
    product_description.append(("🖼️ Imagem", image_url))
    product_description.append(("🔗 Link", product_url))
    product_description.append(("📋 Caraterísticas", features))

    # Adding the product to the dictionary
    products_dict[title] = product_description


print("=== 📦 Produtos Extraídos ===")
for key,product in products_dict.items():
    print("--------------------------------------------------")
    print(f"🛒 Produto: {key}")
    for item in product:
        if item[0] == "📋 Caraterísticas":
            print(f"{item[0]}: ")
            for feature in item[1]:
                print(f"  - {feature}")
        else:
            print(f"{item[0]}: {item[1]}")