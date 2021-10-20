import  warnings
warnings.filterwarnings(action='ignore')
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options) #in case of error remove "./"

s = input('Enter the name of the book\n')
s = s.strip()
s = s.replace(' ','+')
url = 'https://www.goodreads.com/search?q='+s
driver.get(url)
url = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a/span')
driver.execute_script("arguments[0].click();", url)
try:
    popup=driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button/img')
    driver.execute_script("arguments[0].click();", popup)
except: pass

more = driver.find_element_by_css_selector('#description a')
driver.execute_script("arguments[0].click();", more)
description = driver.find_element_by_css_selector('#description').text
print(description)
