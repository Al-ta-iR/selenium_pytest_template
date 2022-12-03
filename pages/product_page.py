# Описать .. метод для добавления в корзину

# Методы проверки
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), \
            "Button for add to cart is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def should_be_button_review(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_REVIEW), \
            "Button for review is not presented"

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button.click()

    def should_be_product_page(self):
        self.should_be_button_add_to_cart()
        self.should_be_login_link()
        self.should_be_button_review()
        self.add_to_cart()
        self.solve_quiz_and_get_code()
