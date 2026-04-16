from fastapi import FastAPI
from scraper import pegar_preco
from database import criar_tabela_produtos, criar_tabela_precos
from database import buscar_historico
from database import salvar_preco, ultimo_preco, adicionar_produto 

app = FastAPI()

# cria tabela ao iniciar
criar_tabela_produtos()

@app.get("/")
def home():
    return {"msg": "API rodando"}

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

from database import (
    criar_tabela_produtos,
    adicionar_produto,
    listar_produtos
)
criar_tabela_produtos()

@app.post("/produto")
def adicionar(url: str, email: str):
    adicionar_produto(url, email)
    return {"msg": "Produto adicionado"}

@app.get("/produtos")
def produtos():
    return listar_produtos()
