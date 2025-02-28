import re

#Exercício 1
texto = """A 03/01/2022, Pedro viajou para a praia com a sua família.
Eles ficaram hospedados num hotel e aproveitaram o sol e o mar durante toda a semana.
Mais tarde, no dia 12/01/2022, Pedro voltou para casa e começou a trabalhar num novo projeto.
Ele passou muitas horas no escritório, mas finalmente terminou o projeto a 15/01/2022."""


def iso_8601(texto):
    return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', texto)

print(iso_8601(texto))


#Exercício 7
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