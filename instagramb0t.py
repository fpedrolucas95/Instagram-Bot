from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Inicializar o driver do navegador
driver = webdriver.Firefox()

# Acessar o Instagram
driver.get("https://www.instagram.com/")

# Aguardar até que a página carregue
time.sleep(3)

# Monitorar se o usuário já fez o login
while True:
    try:
        # Procurar por usuários aleatórios com base na localização
        location_search = driver.find_element_by_css_selector('div._aacl._aacp._aacu._aacx._aada')
        location_search.click()
        location_search.send_keys("NOME_DA_LOCALIZACAO")
        location_search.send_keys(Keys.RETURN)
        time.sleep(2)
        break
    except:
        time.sleep(2)

# Selecionar um usuário aleatório
users = driver.find_elements_by_xpath('//a[@class="z556c"]')
random_user = random.choice(users)
random_user.click()
time.sleep(2)

# Definir o número de vezes que o script deve executar as ações
num_iterations = 10

# Executar as ações diversas vezes
for i in range(num_iterations):
    # Curtir o post
    like_button = driver.find_element_by_xpath('//button[@class="wpO6b "]')
    like_button.click()
    time.sleep(random.randint(30, 60)) # Aguardar um tempo aleatório antes da próxima ação

    # Seguir o usuário
    follow_button = driver.find_element_by_xpath('//button[contains(text(), "Seguir")]')
    follow_button.click()
    time.sleep(random.randint(30, 60)) # Aguardar um tempo aleatório antes da próxima ação

    # Comentar no post
    comment_box = driver.find_element_by_xpath('//textarea[@placeholder="Adicione um comentário…"]')
    comment_box.send_keys("Que legal!")
    comment_box.send_keys(Keys.RETURN)
    time.sleep(random.randint(30, 60)) # Aguardar um tempo aleatório antes da próxima ação

#fechar o driver do navegador
driver.close()
