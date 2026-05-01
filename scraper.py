from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_price(url):
    options = Options()
    # NÃO usar headless por enquanto

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        wait = WebDriverWait(driver, 15)

        # espera o preço aparecer (usando XPath mais confiável)
        price_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h4[contains(., 'R$')]")
            )
        )

        price = price_element.text

        print("DEBUG preço bruto:", price)

        price = price.replace("R$", "").replace(".", "").replace(",", ".").strip()

        return float(price)

    except Exception as e:
        print("Erro detalhado:", e)
        return None

    finally:
        driver.quit()