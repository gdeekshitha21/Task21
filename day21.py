driver.webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
if driver.get_cookies:
print("cookies before login:", driver.get_cookies())
else
print(print("cookies after login:", driver.get_cookies))
driver.quit()