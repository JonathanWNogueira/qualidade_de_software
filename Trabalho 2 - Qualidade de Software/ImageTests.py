from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testPhoenixImage(driver):
    try: 
        driver.get("https://www.phoenix.edu/")

        img_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="header-container"]/div[2]/div[1]/a/picture/img'))
        )
        img_visibility = img_element.is_displayed()

        assert img_visibility == True

        print("testPhoenixImage succeeded")

    except Exception as e:
        print("testInstagramUopx failed")

        driver.implicitly_wait(0.5)
def testRandomPeopleImage(driver):
    try:
        driver.get("https://www.phoenix.edu/")

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="container-58b87fc75d"]/div/div/div[2]/div/div/div[1]/div/div/a/span'))
        )
        element.click()

        element_to_view = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[3]/div/div[1]/img'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", element_to_view)

        img_visibility = element_to_view.is_displayed() # Verifica se a imagem está visível

        assert img_visibility == True

        print("testRandomPeopleImage succeeded")

        driver.implicitly_wait(0.5)
    except Exception as e:
        print("testInstagramUopx failed")