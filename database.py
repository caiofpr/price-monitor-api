import sqlite3

def conectar():
    return sqlite3.connect("precos.db")


# -------------------------
# TABELA PRODUTOS
# -------------------------
def criar_tabela_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            email TEXT
        )
    """)

    conn.commit()
    conn.close()


def adicionar_produto(url, email):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO produtos (url, email) VALUES (?, ?)",
            (url, email)
        )
        conn.commit()
    except Exception as e:
        print("Erro ao inserir produto:", e)

    conn.close()


def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT url, email FROM produtos")
    dados = cursor.fetchall()

    conn.close()

    return [{"url": u, "email": e} for (u, e) in dados]


# -------------------------
# TABELA PREÇOS
# -------------------------
def criar_tabela_precos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS precos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            preco REAL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def salvar_preco(url, preco):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO precos (url, preco) VALUES (?, ?)",
        (url, float(preco))
    )

    conn.commit()
    conn.close()


def buscar_historico(url):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT preco, data FROM precos WHERE url = ? ORDER BY data DESC",
        (url,)
    )

    dados = cursor.fetchall()
    conn.close()

    return [{"preco": p, "data": d} for (p, d) in dados]


def ultimo_preco(url):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT preco FROM precos WHERE url = ? ORDER BY data DESC LIMIT 1",
        (url,)
    )

    resultado = cursor.fetchone()
    conn.close()

    return resultado[0] if resultado else None