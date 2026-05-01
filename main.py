from scraper import get_price
from database import create_table, save_price, get_last_price, get_price_history

create_table()

while True:
    url = input("URL (ou 'sair' / 'historico'): ")

    if url.lower() == "sair":
        break

    if url.lower() == "historico":
        url_hist = input("Digite a URL do produto: ")
        history = get_price_history(url_hist)

        if history:
            print("\nHistórico de preços:\n")
            for price, date in history:
                print(f"Data: {date} | Preço: R$ {price:.2f}")
            print()
        else:
            print("Nenhum histórico encontrado.\n")

        continue

    price = get_price(url)

    if price is not None:
        print(f"Preço atual: R$ {price:.2f}")

        last_price = get_last_price(url)

        if last_price is not None:
            print(f"Preço anterior: R$ {last_price:.2f}")

            if price < last_price:
                print(" O PREÇO CAIU!")
                print(f"Economia: R$ {last_price - price:.2f}")

            elif price > last_price:
                print("O preço aumentou")

            else:
                print("O preço não mudou")

        else:
            print("Primeiro registro desse produto")

        save_price(url, price)
        print("Preço salvo no banco!\n")

    else:
        print("Erro! Não foi possível obter o preço\n")