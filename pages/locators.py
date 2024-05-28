class BasePageLocators:
    LOGIN_LINK = ('css selector', "#login_link")
    BASKET_BUTTON = ('css selector', "span[class='btn-group'] a")
    LOGIN_LINK_INVALID = ('css selector', "#login_link_inc")
    USER_ICON = ('css selector', ".icon-user")
class MainPageLocators():
    LOGIN_LINK = ('css selector', "#login_link")
class LoginPageLocators():
    LOGIN_FORM = ('xpath', '//form[@id = "login_form"]')
    REGISTER_FORM = ('xpath', '//form[@id = "register_form"]')
    REGISTRATION_EMAIL = ('xpath', '//input[@name = "registration-email"]')
    REGISTRATION_PASSWORD1 = ('xpath', '//input[@name = "registration-password1"]')
    REGISTRATION_PASSWORD2 = ('xpath', '//input[@name = "registration-password2"]')
    REGISTRATION_BUTTON = ('xpath', '//button[@name = "registration_submit"]')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = ('xpath', '//button[contains(@class, "btn-add-to-basket")]')
    PRODUCT_NAME = ('css selector', "div h1")
    ADD_TO_BASKET_MESSAGE = ('css selector', "div.alertinner > strong")
    PRODUCT_PRICE = ('css selector', ".product_main p[class='price_color']")
    BASKET_PRICE = ('css selector', "div.alert div p strong")
class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = ('css selector', "#content_inner")
    ITEMS_TO_BUY_NOW = ('css selector', ".basket-items")
