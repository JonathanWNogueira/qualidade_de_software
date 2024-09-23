from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testFailLogin(driver):
    try:
        driver.get("https://phoenix.edu")

        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cmp-header_button-upper")) 
        )
        button.click()

        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "callback_1"))  #aguarda até o campo de login aparecer 
        )
        
        password = driver.find_element(By.NAME, "callback_2") 
        
        username.send_keys("test")
        password.send_keys("test")
        
        login = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
        login.click()

        fail_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="callbacksPanel"]/div[1]/div[2]/div/div/div/div[1]'))  
        )

        img_visibility = fail_message.is_displayed() 

        assert img_visibility == True
        
        print("testFailLogin succeeded")

        driver.implicitly_wait(0.5)
    except Exception as e:
        print("testFailLogin failed")