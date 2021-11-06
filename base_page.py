from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс.
    """

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """
        Открытие страницы.
        """
        self.driver.get(self.url)

    def find_element(self, locator, timeout=10):
        """
        Поиск элемента по локатору.
        :param locator: локатор искомого элемента
        :param timeout: таймаут
        :return: найденный элемент либо ничего, если элемент не был найден
        """
        try:
            ec_pr = EC.presence_of_element_located(locator)
            element = WebDriverWait(self.driver, timeout).until(ec_pr)
            return element
        except TimeoutException:
            return None
