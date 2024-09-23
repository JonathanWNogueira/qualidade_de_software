from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def testMainTitle(driver):
    try:
        driver.get("https://www.phoenix.edu/")

        title = driver.title
        assert title == "Online College for Working Adults - University of Phoenix"

        print("testMainTitle succeeded")

    except Exception as e:
        print("testSearchTextbox failed:")

def testUniversityTitle(driver):
    try:

        driver.get("https://www.phoenix.edu/")

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="container-58b87fc75d"]/div/div/div[2]/div/div/div[2]/div/div/a/span'))
        )
        element.click()

        title = driver.title
        assert title == "Find Online Degree Programs from the University of Phoenix"

        print("testUniversityTitle succeeded")

        driver.implicitly_wait(0.5)
    except Exception as e:
        print("testSearchTextbox failed:")