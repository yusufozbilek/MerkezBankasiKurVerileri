from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from CurrencyClass import TcmbCurrencyData

CurrencyObj = TcmbCurrencyData()

print(CurrencyObj.GetCurrency("USD/TRY"))
print("#################################")
print(CurrencyObj.GetCrossRate("USD/RUB"))
print("#################################")
print(CurrencyObj.GetAllCurrency())
print("#################################")
print(CurrencyObj.GetAllCrossRates())
print("#################################")
print(CurrencyObj.GetCurrencyLenght())
print("#################################")
print(CurrencyObj.GetCrossRateLenght())
