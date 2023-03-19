from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_LINK = (By.NAME, "registration_submit")
    LOGIN_LINK = (By.NAME, "login_submit")
    EMAIL_FOR_REGISTRATION = (By.NAME, "registration-email")
    PASSWORD_FOR_REGISTRATION = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD = (By.NAME, "registration-password2")

class ProductPageLocators():
    BUY_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    EXPECTED_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    EXPECTED_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ACTUAL_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    ACTUAL_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CLASS_NAME, "btn-group .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    MESSAGE = (By.CSS_SELECTOR, "div#content_inner > p")

