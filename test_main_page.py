from main_page import MainPage


def test_title(driver):
    """
    Проверка отображения ShiningPanda в заголовке страницы".
    :param driver: экземпляр класса драйвера Chrome
    """
    main_page = MainPage(driver)
    main_page.open()
    assert main_page.get_title() == "ShiningPanda", "Incorrect page title!"
