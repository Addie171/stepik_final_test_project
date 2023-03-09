from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_LINK = (By.NAME, "registration_submit")
    LOGIN_LINK = (By.NAME, "login_submit")

class ProductPageLocators():
    BUY_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    EXPECTED_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    EXPECTED_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ACTUAL_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    ACTUAL_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")