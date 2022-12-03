from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
uri_promo = '/?promo='
promo_new_year = 'newYear'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link+uri_promo+promo_new_year)
    page.open()
    page.should_be_product_page()
