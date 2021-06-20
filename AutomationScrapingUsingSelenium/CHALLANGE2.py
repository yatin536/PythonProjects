from Drivers import driver
from selenium.webdriver.common.keys import Keys
driver.get("http://secure-retreat-92358.herokuapp.com/")
FirstName=driver.find_element_by_name("fName")
FirstName.send_keys("Yatin")
LastName=driver.find_element_by_name("lName")
LastName.send_keys("Singh")
Email=driver.find_element_by_name("email")
Email.send_keys("Yatin0@gmail.com")
Ente=driver.find_element_by_xpath("/html/body/form/button")
Ente.send_keys(Keys.ENTER)
#driver.close()
