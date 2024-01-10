import importations
from importations import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

#Variável global
driver = importations.webdriver.Chrome()

#Recebe as credenciais do usuário e faz login no site
def extract_files():
    print("Você iniciou o script de extração de dados! \nInforme o link da página de login e depois digite suas credenciais para podermos coletar os dados e fazer o download no seu PC")
    url_login = input('\nLogin website: ')
    print('\nAgora digite suas credenciais:\n')
    username = input('username = ')
    password = input('password = ')
    driver.get(url_login)
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("xpath",'//button').click()
    
    driver.implicitly_wait(4)

     # Verifica se o botão está ativo como "Em andamento"
    if  driver.find_element(By.ID, "groupingdropdown").text != "Todos (exceto removidos da visualização)":
        # Clica no botão de filtro para abrir as opções
        driver.find_element(By.ID, "groupingdropdown").click()

        # Clica para mostrar todos os cursos usando JavaScript
        mostrar_todos_cursos = driver.find_element(By.XPATH, "//a[contains(@aria-label, 'Mostrar todos os cursos exceto os removidos da visualização')]")
        driver.execute_script("arguments[0].click();", mostrar_todos_cursos)

    # Itera por todas as páginas das UCs e faz o download de todos os arquivos
    total_materias_disponiveis = int(driver.find_element(By.XPATH, "//div[contains(@id, 'courses-view-')]").get_attribute("data-totalcoursecount"))
    contador = 0
    driver.maximize_window()

    for i in range(total_materias_disponiveis):
        print(i)
        driver.implicitly_wait(4)
        materia = driver.find_elements(By.CSS_SELECTOR, "a.aalink.coursename")[i]
        print(materia.text[14:])
    
        if materia.get_attribute("href"):
            contador += 1
            materia.click()
            driver.implicitly_wait(4)
            
            driver.back()

            driver.implicitly_wait(5)
            # Scroll na página a cada 3 iterações
            if i % 3 == 0 and i > 0: 
                driver.execute_script("window.scrollTo(0, 200);")
        
        if contador >= total_materias_disponiveis:
            break

    # Fecha a conexão com o webdriver
    driver.close()

extract_files()


