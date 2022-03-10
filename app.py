from selenium import webdriver
from config import edge_driver_path

# Arrange

username = "your username"
password = "your password"

browser = webdriver.Edge(edge_driver_path)
browser.get('https://github.com/login')

username_box = browser.find_element_by_id("login_field")
username_box.send_keys(username)

password_box = browser.find_element_by_id("password")
password_box.send_keys(password)

# Action

password_box.submit()

# Assert

assert "erasmosoares" in browser.page_source 

browser.quit()
