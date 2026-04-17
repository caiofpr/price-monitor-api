import smtplib
from email.mime.text import MIMEText

EMAIL_REMETENTE = "monitorapiemail@gmail.com"
SENHA_APP = "pndh ooop frkf mabt"

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

        print(f"Email enviado para {destino}")

    except Exception as e:
        print("Erro ao enviar email:", e)

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