from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

url = "https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+page+site+area/bugun"

driver.get(url)
Data = driver.find_element(By.ID,"kurlarContainer")

tablo1 = Data.find_elements(By.CLASS_NAME,"kurlarTablo")[0]
elements = tablo1.find_element(By.TAG_NAME,"tbody")
subjects = elements = elements.find_elements(By.TAG_NAME, "tr")
os.system("cls")
print("Currency"+ " " + "forex_Buy" + " " + "forex_Sell")
for sub in subjects:
    currency_Code = sub.find_element(By.TAG_NAME,"td").text
    forex_Buy = sub.find_elements(By.CLASS_NAME,"deger")[0].text
    forex_Sell = sub.find_elements(By.CLASS_NAME,"deger")[1].text

    print(currency_Code + " " + forex_Buy + " " + forex_Sell)
