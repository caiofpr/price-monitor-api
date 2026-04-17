import time
from scraper import pegar_preco
from database import listar_produtos, salvar_preco, ultimo_preco
from email_service import enviar_email  # se já tiver

def monitorar():
    while True:
        produtos = listar_produtos()

        for item in produtos:
            url = item["url"]
            email = item["email"]

            resultado = pegar_preco(url)

            if "preco" in resultado:
                preco_atual = float(resultado["preco"])
                ultimo = ultimo_preco(url)

                if ultimo is None or preco_atual != ultimo:
                    salvar_preco(url, preco_atual)

                    if ultimo and preco_atual < ultimo:
                        enviar_email(email, url, preco_atual)

        print("Aguardando 60 segundos...")
        time.sleep(60)
