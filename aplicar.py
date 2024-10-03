import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def aplicar_vaga(empresa,vaga):

    browser = webdriver.Firefox()

    browser.get(f'https://{empresa}.gupy.io/candidates/jobs/{vaga}/apply')
    #browser.get('https://login.gupy.io/candidates/signin?int_ref=menu-institucional')

    botao1 = browser.find_element(By.ID,'password-access-button')
    botao1.click()

    login = browser.find_element(By.NAME,'username')
    login.send_keys('usuario')
    senha = browser.find_element(By.NAME,'password')
    senha.send_keys('''senha''')

    botao2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/form/button')
    botao2.click()

##########################################3

    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div[2]/button').click()
    
    except:
        browser.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div[2]/button').click()

    time.sleep(1)

    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div[2]/button').click()
    
    except:
        browser.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div[2]/button').click()

    try:
        browser.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div[2]/button').click()
    
    except:
        browser.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div[2]/button').click()
      
    browser.find_element(By.XPATH,'//*[@id="dialog-give-up-personalization-step"]').click()

aplicar_vaga('cinpal',7143682)
