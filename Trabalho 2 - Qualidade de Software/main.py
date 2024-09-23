from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from TitleTests import *
from ButtonTests import *
from ImageTests import *
from HyperlinkTests import *
from TextboxTest import *
from DropDownTests import *
from VideoTest import *
from SubscribeTests import *
from ScrollTest import *
from FailLoginTest import *

def testComponents():
    options = Options()
    # options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1500, 1500)

    testDatesButton(driver)

    testEmailButton(driver)

    testDropDown(driver)

    testInstagramUopx(driver)

    testLinkedinLink(driver)

    testPhoenixImage(driver)

    testRandomPeopleImage(driver)

    testFailLogin(driver)

    testScroll(driver)

    testBackToTop(driver)

    testSubscribe(driver)

    testSearchTextbox(driver)

    testMainTitle(driver)

    testUniversityTitle(driver) 

    testVideo(driver)

    driver.quit()

testComponents()