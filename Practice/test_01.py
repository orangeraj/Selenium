#test case 01
#https://opensource-demo.orangehrmlive.com

from selenium import webdriver
# Specify the path to the GeckoDriver executable
chrome_driver_path = "C:\Drivers\chromedriver.exe"
# Create a new instance of the Firefox browser with the GeckoDriver executable
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# Open a website
driver.get("https://opensource-demo.orangehrmlive.com/")

#driver.find_element_by_css_selector("password").send_keys("abc")







# Close the browser
#driver.quit()
