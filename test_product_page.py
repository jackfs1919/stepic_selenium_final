from .pages.product_page import ProductPage
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
def test_guest_should_see_add_button(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
def test_guest_can_go_to_add_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()