from base_page import BasePage
from main_page_locators import MainPageLocators


class MainPage(BasePage):
    """
    Класс страницы сайта.
    """
    URL = "https://plugins.jenkins.io/shiningpanda"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def get_title(self):
        title = self.find_element(MainPageLocators.MAIN_PAGE_TITLE_LOCATORS)
        return title.text
