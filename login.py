import importations

# Global Variables
driver = importations.webdriver.Chrome()

# Functions
def login_at_page(url_login, username, password):
    driver.get(url_login)
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("xpath",'//button').click()

