from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Класс локаторов главной страницы.
    """
    MAIN_PAGE_TITLE_LOCATORS = (By.CSS_SELECTOR, ".title-wrapper>.title")
