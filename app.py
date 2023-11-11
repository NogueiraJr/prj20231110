import requests
from bs4 import BeautifulSoup

url = "https://engage.luu.org.uk/groups?utm_source=luuorguk&utm_campaign=clubsocpage"

# Faz a requisição HTTP
response = requests.get(url)
print(response)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Analisa o conteúdo da página com BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrando todos os cards (pode ser necessário ajustar esta parte dependendo da estrutura HTML do site)
    cards = soup.find_all("div", class_="p-6 space-y-2")

    # Itera sobre cada card e extrai título e sub-título
    for card in cards:
        title = card.find("h2", class_="font-bold text-xl text-luu-yellow-300").text.strip()
        subtitle = card.find("a", class_="uppercase text-sm text-luu-green-50").text.strip()

        # Exibe os resultados
        print(f"Título: {title}\nSubtítulo: {subtitle}\n{'='*30}")
else:
    print(f"Erro {response.status_code} ao acessar a página.")
