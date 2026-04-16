from playwright.sync_api import sync_playwright

def pegar_preco(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
<<<<<<< HEAD
                headless=True,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                    "--disable-setuid-sandbox"
                ]
=======
                headless=False,
                args=["--disable-blink-features=AutomationControlled"]
>>>>>>> a4ab5bf514157f8d8ef6770737c607a2d24b954e
            )

            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            )

            page = context.new_page()
            page.goto(url, timeout=60000)
            page.wait_for_timeout(5000)

<<<<<<< HEAD
            def extrair_valor(container):
                inteiro = container.locator(
                    ".andes-money-amount__fraction"
                ).first.inner_text().strip().replace(".", "")

                cents_locator = container.locator(
=======
            # -------------------------------------------------------
            # O Mercado Livre separa o preço em dois elementos HTML:
            #   .andes-money-amount__fraction → parte inteira  (ex: "199" ou "1.299")
            #   .andes-money-amount__cents    → centavos       (ex: "90")
            #
            # IMPORTANTE: a parte inteira pode ter ponto de milhar ("1.299"),
            # então deve-se remover esse ponto ANTES de montar o float.
            # Os centavos são sempre 2 dígitos sem separador.
            #
            # Estrutura de preços no ML:
            #   Com promoção → .ui-pdp-price__original-value  = preço riscado
            #                  .ui-pdp-price__second-line      = preço promocional ✅
            #   Sem promoção → .ui-pdp-price__second-line      = preço normal ✅
            # -------------------------------------------------------

            def extrair_valor(container_locator):
                """
                Extrai float de um container de preço do Mercado Livre.
                Trata corretamente o ponto de milhar na parte inteira.
                """
                # parte inteira: remove ponto de milhar (ex: "1.299" → "1299")
                inteiro_raw = container_locator.locator(
                    ".andes-money-amount__fraction"
                ).first.inner_text()
                inteiro = inteiro_raw.strip().replace(".", "")  # remove milhar

                # centavos: elemento separado, sempre 2 dígitos (ex: "90")
                cents_locator = container_locator.locator(
>>>>>>> a4ab5bf514157f8d8ef6770737c607a2d24b954e
                    ".andes-money-amount__cents"
                ).first

                if cents_locator.count() > 0:
                    centavos = cents_locator.inner_text().strip()
                    return float(f"{inteiro}.{centavos}")
                else:
                    return float(inteiro)

            preco_final = None

<<<<<<< HEAD
            promo = page.locator(
                ".ui-pdp-price__second-line .andes-money-amount"
            ).first

            if promo.count() > 0:
                try:
                    preco_final = extrair_valor(promo)
                except:
                    preco_final = None

            if preco_final is None:
                normal = page.locator("div.ui-pdp-price").first
                preco_final = extrair_valor(normal)
=======
            # 1) Tenta preço PROMOCIONAL (segunda linha — preço com desconto)
            promo_container = page.locator(
                ".ui-pdp-price__second-line .andes-money-amount--cents-superscript"
            ).first

            if promo_container.count() > 0:
                try:
                    preco_final = extrair_valor(promo_container)
                except Exception as e:
                    print(f"[WARN] Falha ao ler preço promocional: {e}")
                    preco_final = None

            # 2) Fallback: container genérico (sem promoção)
            if preco_final is None:
                container = page.locator("div.ui-pdp-price").first
                preco_final = extrair_valor(container)
>>>>>>> a4ab5bf514157f8d8ef6770737c607a2d24b954e

            browser.close()
            return {"preco": preco_final}

    except Exception as e:
        return {"erro": str(e)}


if __name__ == "__main__":
<<<<<<< HEAD
    url = "https://www.mercadolivre.com.br/teclado-gamer-phantom-rainbow-mecanico-switch-brown-cor-de-teclado-preto-idioma-portugus-brasil/p/MLB46094968"
    print(pegar_preco(url))
=======
    url = (
        "https://www.mercadolivre.com.br/teclado-gamer-phantom-rainbow-mecanico"
        "-switch-brown-cor-de-teclado-preto-idioma-portugus-brasil/p/MLB46094968"
    )
    resultado = pegar_preco(url)
    print(resultado)
>>>>>>> a4ab5bf514157f8d8ef6770737c607a2d24b954e
