from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Launching Default Browser")
    yield driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


# Hook for delete/modify environment info in HTML Reports
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('Java_Home', None)
    metadata.pop('Plugins', None)
