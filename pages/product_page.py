# Описать .. метод для добавления в корзину

# Методы проверки
from .base_page import BasePage
from .locators import ProductPageLocators
import time


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

    def get_product_name(self):
        product_name = self.return_element_text(*ProductPageLocators.PRODUCT_NAME)
        return product_name

    def get_product_price(self):
        product_price = self.return_element_text(*ProductPageLocators.PRODUCT_PRICE)
        return product_price

    def get_product_price_in_cart_mini(self):
        product_price_in_cart_mini = self.return_element_text(*ProductPageLocators.PRODUCT_PRICE_IN_CART_MINI)
        return product_price_in_cart_mini

    def get_product_name_in_allert(self):
        product_name_in_allert = self.return_element_text(*ProductPageLocators.PRODUCT_NAME_IN_ALLERT)
        return product_name_in_allert

    def should_be_product_page(self):
        # time.sleep(1)
        self.should_be_button_add_to_cart()
        self.should_be_login_link()
        self.should_be_button_review()
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        self.add_to_cart()
        product_price_in_cart_mini = self.get_product_price_in_cart_mini()
        product_name_in_allert = self.should_be_product_page()
        assert product_price == product_price_in_cart_mini, \
            f'Product price: {product_price_in_cart_mini} \
            does not equals price in cart mini: {product_price_in_cart_mini}'
        assert product_name in product_name_in_allert, \
            f'Product name: {product_name} is not in allert: {product_name_in_allert}'
        self.solve_quiz_and_get_code()