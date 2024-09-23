from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def testDatesButton(driver):
    try:
        driver.get("https://www.phoenix.edu/")
        
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="container-58b87fc75d"]/div/div/div[2]/div/div/div[1]/div/div/a/span')) 
        )
        element.click() # presence_of_element - ficar buscando até aparecer

        url = driver.current_url
        assert url == "https://www.phoenix.edu/cost-savings"
        print("testDatesButton succeded")

        driver.implicitly_wait(0.5)

    except Exception as e:
        print("testDatesButton Failed")

def testEmailButton(driver):
    try:
        driver.get("https://www.phoenix.edu/")

        actions = ActionChains(driver)

        actions.move_by_offset(100, 200).perform()
        
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cx_widget_side_bar"]/div[2]/div/div[1]/img'))
        )
        element.click()

        url = driver.current_url
        assert url == "https://www.phoenix.edu/request/email-us?EmailCaptureSource=EU"
        print("testEmailButton succeeded")

        driver.implicitly_wait(0.5)

    except Exception as e:
        print("testEmailButton failed")