import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
try:
    bcs = "button.bt-add-to-basket"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    def test_added_button(browser):
         browser.get(link)
         # browser.implicitly_wait(5)
         assert browser.find_element(By.CSS_SELECTOR, bcs) , "Кнопка не найдена"
         button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, bcs))
         )
         button.click()
finally:
    print("The finally statement has executed!")
