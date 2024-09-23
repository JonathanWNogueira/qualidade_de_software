from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def testSearchTextbox(driver):
    try:
        driver.get("https://phoenix.edu")
        
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cmp-header_search.search-desktop")) 
        )
        button.click()

        search_box = driver.find_element(By.ID, "searchBox")  # Aguarda até poder clilcar no campo de pesquisa

        search_box.send_keys("test")
        search_box.send_keys(Keys.ENTER)

        url = driver.current_url
        assert url == "https://www.phoenix.edu/search.html?q=test"

        print("testSearchTextbox succeeded")

        driver.implicitly_wait(0.5)
    except Exception as e:
        print("testSearchTextbox failed:")