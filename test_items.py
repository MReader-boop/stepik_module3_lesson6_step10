from selenium.webdriver.common.by import By

def test_find_basket_button(browser):
    print('Browser initialised!')
    browser.implicitly_wait(10)
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add_to_basket_button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket') #find_elements находит элементы и кладёт их в массив. Если массив пустой, значит мы не нашли искомую кнопку.
    assert add_to_basket_button, '"Add to basket" button not found!'