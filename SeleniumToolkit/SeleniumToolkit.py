from selenium import webdriver
from time import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
class SeleniumToolKit: 
    def set_webdriver(self, driver):
        self.driver = driver

    def scroll_down(self):
        element = self.driver.find_element_by_tag_name('html');
        element.send_keys(Keys.END)

    def get_checkbox_by_text(self , text):
        for i in range(20):
            try:
               element =  self.driver.find_element_by_xpath(".//*[contains(text(),'"+text+"')]")
               return element
               break
            except NoSuchElementException as e:
               time.sleep(1)

        else: 
            return None

    def open_page_in_newtab(self,link):
       self.driver.execute_script('window.open("'+link+'", "_blank");')
    


    def close_current_tab(self):
 
        body = self.driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL + 'w')
        
    def select_all_text(self, element):



driver = webdriver.Chrome('f:/chrome\chromedriver.exe')
sel = SeleniumToolKit()
sel.set_webdriver(driver)
driver.get('http://localhost')
sel.open_page_in_newtab('http://localhost/dvwa')
 
sel.close_current_tab()