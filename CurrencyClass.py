from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class TcmbCurrencyData:
    def __init__(self):
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        self.driver = webdriver.Chrome(options=op)
        url = "https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+page+site+area/bugun"
        self.driver.get(url)
        self.Data = self.driver.find_element(By.ID,"kurlarContainer")
    def GetAllCurrency(self,Currency):
        currencyList = [[]]
        tablo1 = self.Data.find_elements(By.CLASS_NAME,"kurlarTablo")[0]
        elements = tablo1.find_element(By.TAG_NAME,"tbody")
        subjects = elements = elements.find_elements(By.TAG_NAME, "tr")
        for sub in subjects:
            currency_Code = sub.find_element(By.TAG_NAME,"td").text
            unit = sub.find_elements(By.CLASS_NAME,"para.birim")[0].text
            currencyName = sub.find_elements(By.CLASS_NAME,"para")[0].text
            forex_Buy = sub.find_elements(By.CLASS_NAME,"deger")[0].text
            forex_Sell = sub.find_elements(By.CLASS_NAME,"deger")[1].text
            effective_buy = sub.find_elements(By.CLASS_NAME,"deger.efdeger")[0].text
            effective_sell = sub.find_elements(By.CLASS_NAME,"deger.efdeger")[1].text
            currencyList.append([currency_Code,unit,currencyName,forex_Buy,forex_Sell,effective_buy,effective_sell])
        return currencyList
