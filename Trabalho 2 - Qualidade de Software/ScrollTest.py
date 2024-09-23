import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def testScroll(driver):
    try: 
        driver.get("https://www.phoenix.edu/")

        actions = ActionChains(driver)

        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.DOWN)

        actions.move_by_offset(100, 200).perform()

        time.sleep(1) 

        scroll_position = driver.execute_script("return window.pageYOffset;")
        assert scroll_position == 40

        print("testScroll succeeded")

        driver.implicitly_wait(0.5)
    except AssertionError:
        raise Exception("testScroll failed. Posição esperada era 40. Posição recebida:", scroll_position)
    

def testBackToTop(driver):
    try: 
        driver.get("https://www.mypromomall.com/phoenixstore")

        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.DOWN * 10)

        time.sleep(1)

        back_to_top_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "back-to-top"))
        )
        back_to_top_button.click()

        time.sleep(2)

        assert driver.execute_script("return window.pageYOffset;") == 0

        print("testBackToTop succeeded")

        driver.implicitly_wait(0.5)
    except Exception as e:
        print("testBackToTop failed")
