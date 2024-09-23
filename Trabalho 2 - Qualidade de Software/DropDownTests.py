from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def testDropDown(driver):
    try:
        driver.get("https://www.phoenix.edu/")

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="embed-40af6299b2"]/div/div/button/h3'))
        )
        driver.execute_script("arguments[0].click();", element)

        menu = driver.find_element(By.XPATH, '//*[@id="embed-40af6299b2"]/div/div/div')
        menu_style = menu.get_attribute("style") # "estilo" do background quando o dropdown está ativado

        assert "display: block" in menu_style

        print("testDropDown succeeded")

        driver.implicitly_wait(0.5)

    except Exception as e:
        print("testDropDown failed")