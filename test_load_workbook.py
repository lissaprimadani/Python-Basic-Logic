'''
This logic help to load workbook
It's help to automate taking datas from workbook
'''

from email.message import Message
from turtle import title
from selenium import webdriver
import pytest
from openpyxl import load_workbook
import time
import pyautogui


#adjust with folder address on your computer + file name
woorkbook = load_workbook(filename="E:\BELAJARQA\Python-Basic-Logic\workbook.xlsx") 
#This shows which one sheet you will take
SheetRange1 = woorkbook['Sheet1']
SheetRange2 = woorkbook['Sheet2']



driver = webdriver.Chrome()
driver.maximize_window()

def test_load1():
    i = 2
    while i <=len(SheetRange1['A']):
        LinkWeb = SheetRange1['A'+str(i)].value
        AssertTitle = SheetRange1['B'+str(i)].value

        driver.get(LinkWeb)
        time.sleep(5)
        Title = driver.title
        assert Title == AssertTitle
        i = i + 1

def test_load2():
    i = 2
    while i <=len(SheetRange2['B']):
        Username = SheetRange2['B'+str(i)].value
        Password = SheetRange2['C'+str(i)].value
        Message = SheetRange2['D' +str(i)].value

        driver.get("https://www.instagram.com/")
        time.sleep(5)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(Username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(Password)
        driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(2)
        AssertMessage = driver.find_element_by_xpath('//*[@id="slfErrorAlert"]').text
        assert AssertMessage == Message
        time.sleep(3)
        i = i + 1
