from scraper import get_price
from database import create_table, save_price, get_last_price

# lista de produtos
urls = [
    "https://www.kabum.com.br/produto/907814/placa-de-video-asrock-rx-7600-challenger-pro-oc-amd-radeon-8gb-gddr6-triple-fan-90-ga62zz-00uanf"
]

create_table()

for url in urls:
    print(f"\nVerificando produto: {url}")

    price = get_price(url)

    if price is not None:
        print(f"Preço atual: R$ {price:.2f}")

        last_price = get_last_price(url)

        if last_price is not None:
            if price < last_price:
                print("🔥 PREÇO CAIU!")
                print(f"Economia: R$ {last_price - price:.2f}")

        else:
            print("Primeiro registro")

        save_price(url, price)
        print("Salvo com sucesso")

    else:
        print("Erro ao obter preço")