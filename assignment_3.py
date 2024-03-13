# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the testpages homepage
driver.get("https://testpages.eviltester.com/styled/index.html")
time.sleep(8)


# Test Feature 1: Uploading a file

upload_file = driver.find_element("id","fileuploadtest")
upload_file.click()

# Wait
time.sleep(4)

# Uploading file
upload_input = driver.find_element("id","fileinput")
upload_input.send_keys("C:/Users/jaski/Downloads/Assignment 3.docx")

# Select type of file
select_file_type = driver.find_element("id","itsafile")
select_file_type.click()

# Click on upload button
upload = driver.find_element("xpath","/html/body/div/div[3]/form/div[3]/input")
upload.click()

# Wait
time.sleep(8)

# Navigate to the "Home" page
driver.find_element("xpath","/html/body/div/div[1]/div[1]/a").click()

# Wait
time.sleep(4)



# Test Feature 2: Drag and drop element

drag_drop = driver.find_element("xpath","/html/body/div/ul[1]/li[9]/ul/li[2]/a")
drag_drop.click()

# Wait
time.sleep(4)

# Locate the element to be dragged
source_element = driver.find_element("id","draggable2")
# Locate the element where the source element will be dropped
target_element = driver.find_element("id","droppable1")

# Perform drag-and-drop action
actions = ActionChains(driver)
actions.drag_and_drop(source_element, target_element).perform()

# Wait
time.sleep(8)

# Navigate to the "Home" page
driver.find_element("xpath","/html/body/div/div[1]/div[1]/a").click()

# Wait
time.sleep(4)



# Test Feature 3: File Download

download_file = driver.find_element("xpath","/html/body/div/ul[1]/li[15]/ul/li[2]/a")
download_file.click()

# Wait
time.sleep(4)

download_link = driver.find_element("xpath","/html/body/div/div[3]/p[2]/a/button")
download_link.click()

# Wait
time.sleep(4)

# Navigate to the "Home" page
driver.find_element("xpath","/html/body/div/div[1]/div[1]/a").click()

# Wait
time.sleep(4)



# Test Feature 4: Login

login_page = driver.find_element("id","adminlogin")
login_page.click()

input_username = driver.find_element("id","username")
input_password = driver.find_element("id","password")
login_button = driver.find_element("id","login")

input_username.send_keys("Admin")
input_password.send_keys("AdminPass")

# Wait
time.sleep(4)

login_button.click()

# Wait
time.sleep(8)




# Test Feature 5: Logout

logout_user = driver.find_element("id","navadminlogout")
logout_user.click()

# Wait
time.sleep(4)

# Navigate to the "Home" page
driver.find_element("xpath","/html/body/div/div[1]/div[1]/a").click()

# Wait
time.sleep(4)




# Test Feature 6: Form Validation

field_validation = driver.find_element("id","javascriptfieldvalidationtest")
field_validation.click()

# Wait
time.sleep(4)

value_1 = driver.find_element("id","lteq30a")
value_1.send_keys("26")

value_2 = driver.find_element("id","lteq30b")
value_2.send_keys("12")

# Wait
time.sleep(4)

submit_button = driver.find_element("xpath","/html/body/div/div[3]/form/input[1]")
submit_button.click()

# Wait
time.sleep(4)

# Navigate to the "Home" page
driver.find_element("xpath","/html/body/div/div[1]/div[1]/a").click()

# Wait
time.sleep(4)

# Closing the webdriver
driver.close()
