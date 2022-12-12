import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions


@pytest.fixture
def fmn_unauthorized():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

@pytest.fixture
def fmn_authorized():
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}

    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://fmn.apps.ocp.stg.fedoraproject.org/")

    login_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn")
    login_button.click()
    WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.NAME,"login_name"))

    username = driver.find_element(by=By.NAME, value="login_name")
    password = driver.find_element(by=By.NAME, value="login_password")
    submit = driver.find_element(by=By.ID, value="loginbutton")
    username.send_keys("<username>")
    password.send_keys("<apasswrod>")
    submit.click()

    WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.CSS_SELECTOR,".nav-item.dropdown"))
    
    driver.get("https://fmn.apps.ocp.stg.fedoraproject.org/rules")
    yield driver
    driver.quit()
