from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
display = Display(visible=0, size=(800, 600))
display.start()
browser = webdriver.Chrome()
browser.get('https://www.facebook.com/')
print(browser.title)
email_box = browser.find_element_by_xpath('//*[@id="email"]')
email_box.send_keys("User_ID")
password_box = browser.find_element_by_xpath('//*[@id="pass"]')
password_box.send_keys("Password")
login_button = browser.find_element_by_id('u_0_m')
login_button.click()
print(browser.title)
msg_box = browser.find_elements_by_class_name('_2n_9')
msg_box[1].click()
print ("Done")
browser.close()
display.stop()