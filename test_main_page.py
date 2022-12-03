from .pages.login_page import LoginPage
from .pages.main_page import MainPage


link = 'http://selenium1py.pythonanywhere.com/'
# link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'

def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_auth_page(browser):
    url = link + 'ru/accounts/login/'
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_page()
