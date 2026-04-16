from playwright.sync_api import sync_playwright

def pegar_preco(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                    "--disable-setuid-sandbox"
                ]
            )

            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            )

            page = context.new_page()
            page.goto(url, timeout=60000)
            page.wait_for_timeout(5000)

            def extrair_valor(container):
                inteiro = container.locator(
                    ".andes-money-amount__fraction"
                ).first.inner_text().strip().replace(".", "")

                cents_locator = container.locator(
                    ".andes-money-amount__cents"
                ).first

                if cents_locator.count() > 0:
                    centavos = cents_locator.inner_text().strip()
                    return float(f"{inteiro}.{centavos}")
                else:
                    return float(inteiro)

            preco_final = None

            # tenta preço promocional
            promo = page.locator(
                ".ui-pdp-price__second-line .andes-money-amount"
            ).first

            if promo.count() > 0:
                try:
                    preco_final = extrair_valor(promo)
                except:
                    preco_final = None

            # fallback preço normal
            if preco_final is None:
                normal = page.locator("div.ui-pdp-price").first
                preco_final = extrair_valor(normal)

            browser.close()
            return {"preco": preco_final}

    except Exception as e:
        return {"erro": str(e)}


if __name__ == "__main__":
    url = "https://www.mercadolivre.com.br/teclado-gamer-phantom-rainbow-mecanico-switch-brown-cor-de-teclado-preto-idioma-portugus-brasil/p/MLB46094968"
    print(pegar_preco(url))