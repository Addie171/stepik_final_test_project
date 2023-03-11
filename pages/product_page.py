from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_to_basket(self):
        buy_btn = self.browser.find_element(*ProductPageLocators.BUY_BTN)
        buy_btn.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_right_name(self):
        expected_name = self.browser.find_element(*ProductPageLocators.EXPECTED_BOOK_NAME).text
        print('expected_name =', expected_name)
        actual_name = self.browser.find_element(*ProductPageLocators.ACTUAL_BOOK_NAME).text
        print('actual_name =', actual_name)
        assert expected_name == actual_name, "Names are different"

    def should_be_right_price(self):
        expected_price = self.browser.find_element(*ProductPageLocators.EXPECTED_PRICE).text
        print('expected_price =', expected_price)
        actual_price = self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE).text
        print('actual_price =', actual_price)
        assert expected_price == actual_price, "Prices are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

