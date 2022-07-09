from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from CurrencyClass import TcmbCurrencyData

CurrencyObj = TcmbCurrencyData()
for value in range(0,CurrencyObj.GetCrossRateLenght()):
    print(CurrencyObj.GetAllCrossRates()[value])
