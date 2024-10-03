import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options



def achar_empresas():

    options = Options()
    options.add_argument("--headless")

    browser = webdriver.Firefox(options=options)

    empresas = []

    for i in range(0,401,10):
        browser.get(f'view-source:https://www.google.com/search?q=site:https://gupy.io/&start={i}')
        dados = browser.find_element(By.XPATH,'//*[@id="line1"]')
        lista = re.findall(r'https://([a-zA-Z0-9-]+)\.gupy\.io/', dados.text)
        lista = set(lista)

        for j in lista:
            if j not in empresas:
                empresas.append(j)
        
    return(empresas)
                      

with open('empresas.txt', 'w') as f:
    f.write(f'{achar_empresas()}')