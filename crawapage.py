from random import randrange
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options ,service=ChromeService(ChromeDriverManager().install()),)
driver.get("https://aws.amazon.com/vi/route53/what-is-dns/")
driver.implicitly_wait(2)


titles = driver.find_elements(By.XPATH,"//div[@class='title-wrapper']")
noidung = driver.find_elements(By.XPATH,"//div[@class='aws-text-box']")

print(len(noidung))
print(len(titles))
for i in range(len(titles)):
    print( "*", titles[i].text + ":", noidung[i].text )
    print("_________")

driver.close()