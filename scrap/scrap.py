import requests
from bs4 import BeautifulSoup


url = 'https://noticias.uol.com.br/'


response = requests.get(url)


if response.status_code == 200:
    print("Conexão bem-sucedida!")
else:
    print(f"Erro ao acessar a página. Status code: {response.status_code}")
    exit()


soup = BeautifulSoup(response.content, 'html.parser')


titulos = soup.select('h3.thumb-title.title-xsmall.title-lg-small')[:6]


print("Títulos dos 6 primeiros artigos:")
for i, titulo in enumerate(titulos, start=1):
    print(f"{i}. {titulo.text.strip()}")
