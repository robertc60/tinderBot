from selenium import webdriver
from time import sleep
from secrets import email, pw

class tinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        # Selecting log in with fb button
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        # Saving main window to var
        base_window = self.driver.window_handles[0]
        # Select Pop-up window
        popup = self.driver.switch_to_window(self.driver.window_handles[1])
        # Select and input email address
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)
        # Select password field and input password
        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(pw)
        # click login button
        login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login.click()
        # Swap back to main window
        self.driver.switch_to_window(self.driver.window_handles[0])
        # Close location popup
        sleep(1.5)
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        # Close notification popuppopup_2
        sleep(1)
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
        # TODO: login sequence complete, add swipe functionality 
bot = tinderBot()
bot.login()
        