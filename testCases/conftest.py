from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture()
def setup(browser):
    if browser == "firefox":
        driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()), options=setBrowserOptions(browser))
    elif browser in ["edge", "Edge", "chromium"]:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=setBrowserOptions(browser))
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=setBrowserOptions(browser))
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    """This will get the value from CLI/hooks"""
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    """This will return the browser value to setup method"""
    return request.config.getoption("--browser")


def setBrowserOptions(browser):
    if browser == "firefox":
        options = FirefoxOptions()
    elif browser in ["edge", "Edge", "chromium"]:
        options = EdgeOptions()
    else:
        options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1325x744')
    return options


def pytest_configure(config):
    """It is hook for adding environment info to the HTML Report"""
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Vikas'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    """It is hook for delete/Modify Environment info to HTML Report"""
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



