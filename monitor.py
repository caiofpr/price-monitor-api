import time
from scraper import pegar_preco
from database import listar_produtos, salvar_preco, ultimo_preco
from email_service import enviar_email


def monitorar():
    print("Monitoramento iniciado...")

    while True:
        produtos = listar_produtos()

        if not produtos:
            print("Nenhum produto cadastrado...")
        else:
            for produto in produtos:
                url = produto["url"]
                email = produto["email"]

                print(f"Verificando: {url}")

                resultado = pegar_preco(url)

                if "preco" in resultado:
                    preco_atual = float(resultado["preco"])
                    preco_antigo = ultimo_preco(url)

                    print(f"Preço atual: {preco_atual}")
                    print(f"Preço antigo: {preco_antigo}")

                    salvar_preco(url, preco_atual)

                    # 🚨 ALERTA AQUI
                    if preco_antigo and preco_atual < preco_antigo:
                        print("🔥 PREÇO CAIU! Enviando email...")
                        enviar_email(email, url, preco_atual)

                else:
                    print("Erro ao pegar preço:", resultado)

        print("Aguardando 60 segundos...\n")
        time.sleep(60)

