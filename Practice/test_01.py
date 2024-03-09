
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Open a website
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

actual_title = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")
actual_title_text = actual_title.text
expected_title = 'Dashboard'

if actual_title_text == expected_title:
    print("passed")
else:
    print("failed")









#selenium 3
# from selenium import webdriver
# # Specify the path to the GeckoDriver executable
# chrome_driver_path = "C:\Drivers\chromedriver.exe"
# # Create a new instance of the Firefox browser with the GeckoDriver executable
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# # Open a website
# driver.get("https://opensource-demo.orangehrmlive.com/")
#
# driver.implicitly_wait(10)
# driver.find_element_by_name("username").send_keys("Admin")
# driver.find_element_by_name("password").send_keys("admin123")
# driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
#
# actual_title = driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")
# actual_title_text = actual_title.text
# expected_title = 'Dashboard'
# print(actual_title)
# if actual_title_text == expected_title:
#     print("passed")
# else:
#     print("failed")




# Close the browser
#driver.quit()
