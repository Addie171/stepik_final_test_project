import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    #add = browser.find_element(By.CLASS_NAME, "btn-block")
    # add.click()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_about_empty_basket()





