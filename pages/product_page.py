from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_button()

    def should_be_product_url(self):
        assert 'promo=newYear' in self.browser.current_url, "Не страница товара"


    def should_be_product_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Нет кнопки добавления в корзину"


