import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    """
    Запуск и закрытие драйвера Chrome.
    :return: экземпляр класса драйвера Chrome
    """
    driver = webdriver.Chrome(executable_path="c:/driver/chromedriver")
    yield driver
    driver.quit()
