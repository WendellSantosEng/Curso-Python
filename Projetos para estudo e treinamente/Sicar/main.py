from pathlib import Path
import time
from selenium import webdriver # importar webdriver do chrome
from selenium.webdriver.common.by import By # classe q insere elementos na pagina
from selenium.webdriver.common.keys import Keys # botoes da pagina
from selenium.webdriver.support.wait import WebDriverWait # espera por resposta
from selenium.webdriver.support import expected_conditions as EC # juntamente com a espera de resposta

def open_browser_(*options):
    
    ROOT_FOLDER = Path(__file__).parent

    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option) 

    browser = webdriver.Chrome(
        options = chrome_options,
    )

    return browser

if (__name__ == "__main__"):

    TIME_WAIT = 10
    options = ()
    browser = open_browser_(*options)

    browser.get("https://www.car.gov.br/#/consultar")

    search_input = WebDriverWait(browser, TIME_WAIT).until(
        EC.presence_of_element_located(
            (By.ID, "inputConsultar")
        )
    )

    try:
        search_input.send_keys("MT-5107008-70F794891F4446BBB6E7476013E7719A")
        search_input.click()
        TIME_WAIT
    except:
        print(f"Elemento search_input nao encontrado")

