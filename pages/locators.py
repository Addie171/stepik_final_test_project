from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_submit")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_submit")