from selenium import webdriver

chrom_driver="C:\\Users\\Dell\\Desktop\\WorkStation\\Python Practice\\100DaysOfPythonCoding\\Day48-SeleniumAutomation\\WebDriver\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrom_driver,options=options)
