class MainPageLocators():
    LOGIN_LINK = ('css selector', "#login_link")
class LoginPageLocators():
    LOGIN_FORM = ('xpath', '//form[@id = "login_form"]')
    REGISTER_FORM = ('xpath', '//form[@id = "register_form"]')
class ProductPageLocators():
    ADD_BUTTON = ('xpath', '//button[contains(@class, "btn-add-to-basket")]')
