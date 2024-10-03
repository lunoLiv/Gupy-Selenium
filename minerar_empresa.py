from limpar_dados import limpar_dados

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def minerar_empresa(empresa):
    print(empresa)

    options = Options()
    options.add_argument("--headless")
    
    browser = webdriver.Firefox(options=options)
    pagina_inicial = f'{empresa}.gupy.io'

    browser.get(f'view-source:https://{empresa}.gupy.io')
    dados = browser.find_element(By.XPATH,'//*[@id="line1"]')

    #with open(f'{empresa}.txt', 'w') as f:
    #    f.write(f'{limpar_dados(dados.text,empresa)}')

    resultado = limpar_dados(dados.text,empresa)
    browser.close()
    return resultado

