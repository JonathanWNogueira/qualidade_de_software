from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def testSubscribe(driver):
    try:
        driver.get("https://www.phoenix.edu/")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(2)   
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "fullName"))  
        )
        
        email = driver.find_element(By.NAME, "emailAddress")  
        
        username.send_keys("test test")
        email.send_keys("test@test.com")
        
        subscribe = driver.find_element(By.NAME, "submit")  
        subscribe.click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        element_to_view = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "thanksmessage"))
        )

        img_visibility = element_to_view.is_displayed()

        assert img_visibility == True
        
        print("testSubscribe succeeded")

        driver.implicitly_wait(0.5)
    except Exception as e:
        print("testSubscribe failed")