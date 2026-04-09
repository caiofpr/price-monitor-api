import smtplib
from email.mime.text import MIMEText

EMAIL_REMETENTE = "monitorapiemail@gmail.com"
SENHA_APP = "pndh ooop frkf mabt"


def enviar_email(destinatario, url, preco):
    try:
        mensagem = MIMEText(
            f"O preço do produto caiu!\n\n{url}\nNovo preço: R$ {preco}"
        )

        mensagem["Subject"] = "🔥 Alerta de Preço!"
        mensagem["From"] = EMAIL_REMETENTE
        mensagem["To"] = destinatario

        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, SENHA_APP)

        servidor.sendmail(
            EMAIL_REMETENTE,
            destinatario,
            mensagem.as_string()
        )

        servidor.quit()

        print(f"Email enviado para {destinatario}")

    except Exception as e:
        print("Erro ao enviar email:", e)