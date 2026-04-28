import smtplib
from email.mime.text import MIMEText
import os

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA_APP = os.getenv("EMAIL_SENHA")  # senha de app do Gmail

def enviar_email(destino, assunto, mensagem):
    try:
        msg = MIMEText(mensagem)
        msg["Subject"] = assunto
        msg["From"] = EMAIL_REMETENTE
        msg["To"] = destino

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_REMETENTE, SENHA_APP)
            server.send_message(msg)

        print(f"[OK] Email enviado para {destino}")

    except Exception as e:
        print("[ERRO EMAIL]:", e)


def email_boas_vindas(destino, url):
    assunto = "Monitoramento ativado!"

    mensagem = f"""
Seu email foi cadastrado com sucesso ✅

Agora você receberá alertas quando o preço do produto mudar.

Produto monitorado:
{url}

Se você não solicitou isso, ignore este email.
"""

    enviar_email(destino, assunto, mensagem)