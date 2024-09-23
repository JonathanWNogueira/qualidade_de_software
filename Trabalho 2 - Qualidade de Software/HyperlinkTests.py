from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testInstagramUopx(driver):
    try:
        driver.get("https://www.phoenix.edu/")

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="bottom"]/div[2]/div/div[3]/div/span[2]/a/img'))
        )
        driver.execute_script("arguments[0].click();", element)

        driver.switch_to.window(driver.window_handles[1]) #troca de aba

        url = driver.current_url
        assert url == "https://www.instagram.com/uopx/"

        driver.close()

        driver.switch_to.window(driver.window_handles[0]) #retorna pra aba original

        print("testInstagramUopx succeeded")

        driver.implicitly_wait(0.5)
    except Exception as e:
        print("testInstagramUopx failed")

def testLinkedinLink(driver):
    try:
        driver.get("https://www.phoenix.edu/")

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="bottom"]/div[2]/div/div[3]/div/span[3]/a/img'))
        )
        driver.execute_script("arguments[0].click();", element)

        driver.switch_to.window(driver.window_handles[1])

        url = driver.current_url
        assert url == "https://www.linkedin.com/school/university-of-phoenix/"

        driver.close()

        driver.switch_to.window(driver.window_handles[0])

        print("testLinkedinLink succeeded")

        driver.implicitly_wait(0.5)
    except Exception as e:
        print("testLinkedinLink failed")