from fastapi import FastAPI
from scraper import pegar_preco
from database import (
    criar_tabela_produtos,
    criar_tabela_precos,
    buscar_historico,
    salvar_preco,
    ultimo_preco,
    adicionar_produto,
    listar_produtos
)

app = FastAPI()


@app.on_event("startup")
def startup():
    criar_tabela_produtos()
    criar_tabela_precos()


@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/preco")
def preco(url: str):
    resultado = pegar_preco(url)

    if "preco" in resultado:
        preco_atual = float(resultado["preco"])
        ultimo = ultimo_preco(url)

        if ultimo is None or preco_atual != ultimo:
            salvar_preco(url, preco_atual)

    return resultado

@app.get("/historico")
def historico(url: str):
    return buscar_historico(url)


@app.post("/produto")
def adicionar(url: str, email: str):
    adicionar_produto(url, email)
    return {"msg": "Produto adicionado"}

@app.get("/produtos")
def produtos():
    return listar_produtos()

@app.get("/monitorar")
def monitorar():
    produtos = listar_produtos()

    for item in produtos:
        url = item["url"]

        resultado = pegar_preco(url)

        if "preco" in resultado:
            preco_atual = float(resultado["preco"])
            ultimo = ultimo_preco(url)

            if ultimo is None or preco_atual != ultimo:
                salvar_preco(url, preco_atual)

    return {"status": "monitoramento executado"}