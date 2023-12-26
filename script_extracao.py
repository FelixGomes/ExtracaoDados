import importations
from bs4 import BeautifulSoup
import requests
import login

#Global Variables
driver = importations.webdriver.Chrome()

#Recebe as credenciais do usuário e faz login no site
def user_login():
    print("Você iniciou o script de extração de dados! \nInforme o link da página de login e depois digite suas credenciais para podermos coletar os dados e fazer o download no seu PC")
    url_login = input('\nLogin website: ')
    print('\nAgora digite suas credenciais:\n')
    username = input('username = ')
    password = input('password = ')

    login.login_at_page(url_login, username, password)
    
    extract_files()

#Extrai os arquivos
def  extract_files():
    url_source_website = input("Digite o URL do qual deseja extrair os arquivos: ")
    

    driver.get(url_source_website)

    #to see the whole html content at command line
    html = requests.get(url_source_website).content
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

    driver.close()

user_login()


