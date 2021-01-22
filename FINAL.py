from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        browser = webdriver.Edge()
        driver = self.driver
        driver.get("https://sathyabama.cognibot.in/?redirect=0")
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_xpath("//section[@id='region-main']/div/div[2]/div/div").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("38110201")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("HrithikLMS01#")
        driver.find_element_by_id("loginbtn").click()
        driver.find_element_by_xpath("//img[contains(@src,'https://sathyabama.cognibot.in/theme/image.php/klass/core/1606143158/u/f2')]").click()
        driver.find_element_by_id("actionmenuaction-1").click()
        driver.find_element_by_xpath("//div[@id='nav-notification-popover-container']/div/i").click()
        element = WebDriverWait(browser, 3000).until(EC.presence_of_element_located((By.XPATH,"//div[@id='nav-notification-popover-container']/div/i")))

        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
