from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(20)

    email = driver.find_element_by_name("username")
    email.clear()
    email.send_keys("me.anupsamanta@gmail.com")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("instaPassword")
    password.send_keys(Keys.RETURN)
    time.sleep(10)
    alertbox = driver.find_element_by_class_name("aOOlW")
    alertbox.click()
    time.sleep(2)
    i = 1
    while True:
        time.sleep(10)
        driver.execute_script('window.scrollBy(0, 1000)')
        time.sleep(10)
        like = driver.find_element_by_class_name("_8-yf5")
        like.click()
        print(i, " Posts liked")
        i = i + 1
