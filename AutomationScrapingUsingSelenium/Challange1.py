from selenium import webdriver



chrom_driver="C:\\Users\\Dell\\Desktop\\WorkStation\\Python Practice\\100DaysOfPythonCoding\\Day48-SeleniumAutomation\\WebDriver\\chromedriver.exe"


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrom_driver,options=options)



driver.get("https://www.python.org/")
Events=driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
Events=(Events.text)
def Convert(string):
    li = list(string.split(" "))
    return li
  
# Driver code    
str1 =Events
print(Convert(str1))

driver.close()