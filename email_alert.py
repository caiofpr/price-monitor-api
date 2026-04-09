import resend

resend.api_key = "re_ALttqUea_CqzvMvJFccULtUFDkJRuCxJT"

def enviar_email(destino, assunto, mensagem):
    try:
        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": destino,
            "subject": assunto,
            "text": mensagem,
        })
        print("📧 Email enviado!")

    except Exception as e:
        print("Erro ao enviar email:", e)