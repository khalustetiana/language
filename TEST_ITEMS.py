import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_element_present(), \
        'Кнопка добавления товара в корзину отсутсвует'
