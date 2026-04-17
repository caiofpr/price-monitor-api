import resend
import os

resend.api_key = os.getenv("RESEND_API_KEY") or raise Exception("RESEND_API_KEY não configurada")

def enviar_email(destino, assunto, mensagem):
    try:
        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": [destino],
            "subject": assunto,
            "text": mensagem,
        })
        print(f"Email enviado para {destino}")

    except Exception as e:
        print("Erro ao enviar email:", e)