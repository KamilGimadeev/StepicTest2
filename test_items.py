import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

try:
    bcs = "button.btn-add-to-basket"
    def test_guest_should_see_login_link(browser):
         # browser.implicitly_wait(5)
         assert browser.find_element(By.CSS_SELECTOR, bcs) , "Кнопка не найдена"
         button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, bcs))
         )
         button.click()
finally:
    print("The finally statement has executed!")