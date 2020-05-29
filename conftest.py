import pytest
from selenium import webdriver
site = 0
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='none',
                     help="Choose interface language")



@pytest.fixture(params = ["Chrome","Firefox"])
def browser(request):
    language = request.config.getoption("language")
    brow = request.param
    if brow == "Chrome" :
        browser = webdriver.Chrome()
    elif brow == "Firefox":
        browser = webdriver.Firefox()
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    yield browser
    browser.quit()