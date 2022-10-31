'''
it's skenario how to get data from the system and then write it into a workbook
first running "pip install openpyxl"
'''

from lib2to3.pgen2 import driver
import time
import openpyxl
from openpyxl import Workbook
import pytest
from selenium import webdriver
from openpyxl import load_workbook
import selenium

driver = webdriver.Chrome()
driver.maximize_window()

#first, adjust your workbook address
wb = load_workbook(filename="E:\\BELAJARQA\\Python-Basic-Logic\\hello_world.xlsx")


#example write 'helloword' into workbook
sheet1 = wb['Sheet 1'] #make sure this sheet is already in your workbook
def test_write1():
    sheet1["A1"] = "Hello"
    sheet1["B1"] = "bro"
    wb.save("E:\\BELAJARQA\\Python-Basic-Logic\\hello_world.xlsx")


#example get data from a website and write into workbook
sheet2 = wb['Sheet 2'] #make sure this sheet is already in your workbook
def test_write2():
    driver.get("https://id-id.facebook.com/")
    sheet2['A2'] = driver.title
    sheet2['B2'] = driver.find_element_by_class_name("_8eso").text
    wb.save("E:\\BELAJARQA\\Python-Basic-Logic\\hello_world.xlsx")

#example get 5 list data from a website and write into workbook (using loops)
sheet3 = wb['Sheet 3']
def test_write3():
    driver.get("https://www.idx.co.id/data-pasar/data-saham/daftar-saham/")
    time.sleep(10)
    i = 2
    while i <= 6:
        sheet3['A'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[1]").text
        sheet3['B'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[2]").text
        sheet3['C'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[3]").text
        sheet3['D'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[4]").text
        sheet3['E'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[5]").text
        sheet3['F'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[6]").text
        wb.save("E:\\BELAJARQA\\Python-Basic-Logic\\hello_world.xlsx")
        i = i+1

#example get all list data from a website and write into workbook (using loops)
sheet4 = wb['Sheet 4']
def test_write4():
    driver.get("https://www.idx.co.id/data-pasar/data-saham/daftar-saham/")
    time.sleep(10)
    i = 2
    j = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i)+"]/td[1]").text
    while i <= len(j):
        sheet4['A'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[1]").text
        sheet4['B'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[2]").text
        sheet4['C'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[3]").text
        sheet4['D'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[4]").text
        sheet4['E'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[5]").text
        sheet4['F'+str(i)] = driver.find_element_by_xpath("//*[@id='stockTable']/tbody/tr["+str(i-1)+"]/td[6]").text
        wb.save("E:\\BELAJARQA\\Python-Basic-Logic\\hello_world.xlsx")
        i = i+1
    
    driver.close()


'''
To help learning more about openpyxl library
https://readthedocs.org/projects/ssopenpyxl/downloads/pdf/2.5.4/
'''