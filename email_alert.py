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