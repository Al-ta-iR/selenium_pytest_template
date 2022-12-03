from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_REVIEW = (By.ID, "write_review")
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CLASS_NAME, "col-sm-6.product_main")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    PRODUCT_PRICE_IN_CART_MINI = (By.CLASS_NAME, "basket-mini.pull-right.hidden-xs")
    PRODUCT_NAME_IN_ALLERT = (By.CLASS_NAME, "alertinner ")

