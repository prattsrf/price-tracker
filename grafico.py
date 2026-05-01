import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_price_history(url):
    # conecta no banco
    conn = sqlite3.connect("prices.db")

    # busca os dados
    query = """
        SELECT price, date FROM prices
        WHERE url = ?
        ORDER BY date ASC
    """

    df = pd.read_sql_query(query, conn, params=(url,))

    conn.close()

    if df.empty:
        print("Nenhum dado encontrado para esse produto.")
        return

    # converte data
    df["date"] = pd.to_datetime(df["date"])

    # cria o gráfico
    plt.figure()
    plt.plot(df["date"], df["price"], marker='o')

    plt.title("Histórico de Preço")
    plt.xlabel("Data")
    plt.ylabel("Preço (R$)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# execução
if __name__ == "__main__":
    url = input("Digite a URL do produto: ")
    plot_price_history(url)