# Requirement
# Python 3.9.0
# selenium  3.141.0
# ChromeDriver 86.0.4240.22

from selenium import webdriver

# update the path where the chromedriver is find
driver = webdriver.Chrome(executable_path="C:/Users/praveend/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('http://ksit.ac.in/')

dropdown = driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[4]/ul/li[2]/a')
cse = dropdown.get_attribute('href')
driver.get(cse)

facklitys_page = driver.find_element_by_xpath('//*[@id="myTab"]/li[11]/a')
facklitys_page.click()
facklitys = driver.find_elements_by_xpath("//div[@class='faculty']")

for facklity in facklitys:
    print("\n")
    info  = facklity.find_elements_by_tag_name('p')   
    for name in info:
        if(name.text):
            print(name.text, end = "         ")
        