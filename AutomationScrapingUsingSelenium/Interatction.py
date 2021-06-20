from selenium import webdriver

chrom_driver="C:\\Users\\Dell\\Desktop\\WorkStation\\Python Practice\\100DaysOfPythonCoding\\Day48-SeleniumAutomation\\WebDriver\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrom_driver,options=options)


driver.get("https://en.wikipedia.org/wiki/Main_Page")
count=driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(count.text)
driver.close()

#CHALLANGE COMPLETED FINALLY