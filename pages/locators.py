from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
class BasketPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    BUTTON_REVIEW = (By.ID, "write_review")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MESSAGE_BLOCK = (By.ID, "messages")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME_IN_ALLERT = (By.CLASS_NAME, "alertinner ")
    PRODUCT_PRICE_IN_CART_MINI = (By.CLASS_NAME, "basket-mini.pull-right.hidden-xs")
    PRODUCT_PRICE_IN_CART_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
