'''
This logic to help you finding local data on computer
When creating testing automation, there will be cases such as downloading documents/file. 
And this logic can help you to make assertions on local files
'''
import os
import glob
import time
import pytest


#to get first data on the folder
def test_GetFirstData():
    dir_name = 'E:\\Dokumen\\test\\' #adjust with folder address on your computer
    list_time = filter(os.path.isfile, glob.glob(dir_name + '*'))
    list_file = sorted(list_time, key=os.path.getmtime)
    first_data = (list_file[0])
    assert first_data== 'E:\\Dokumen\\test\\BUG KURANG.pdf' #adjust with folder address on your computer + file name

#to get last data on the folder
def test_GetLastData():
    dir_name = 'E:\\Dokumen\\test\\' #adjust with folder address on your computer
    list_time = filter(os.path.isfile, glob.glob(dir_name + '*'))
    list_file = sorted(list_time, key=os.path.getmtime)
    last_data = (list_file[-1])
    assert last_data== 'E:\\Dokumen\\test\\photo_2022-08-12_15-44-38.jpg' #adjust with folder address on your computer + file name

