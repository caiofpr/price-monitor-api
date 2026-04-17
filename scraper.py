import requests
from bs4 import BeautifulSoup

def pegar_preco(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        preco_inteiro = soup.select_one(".andes-money-amount__fraction")
        preco_centavos = soup.select_one(".andes-money-amount__cents")

        if preco_inteiro:
            inteiro = preco_inteiro.text.strip().replace(".", "")

            if preco_centavos:
                centavos = preco_centavos.text.strip()
                preco = float(f"{inteiro}.{centavos}")
            else:
                preco = float(inteiro)

            return {"preco": preco}

        return {"erro": "Preço não encontrado"}

    except Exception as e:
        return {"erro": str(e)}