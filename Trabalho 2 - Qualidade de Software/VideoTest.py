from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testVideo(driver):
    try:
        driver.get("https://www.phoenix.edu/student-resources/going-to-class.html")
        
        element_to_view = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cmp-video-play-icon"))
        )
        element_to_view.click()

        video_element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ytp-large-play-button.ytp-button.ytp-large-play-button-red-bg"))
        )
        
        driver.execute_script("arguments[0].play();", video_element)

        url = driver.find_element(By.CLASS_NAME, "video-stream.html5-main-video").get_attribute("src")
        
        assert url == "https://www.youtube.com/watch?v=IAjK834RdGk"

        print("testVideo succeeded")
        
    except Exception:
        print("testVideo failed")