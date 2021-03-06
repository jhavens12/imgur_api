from datetime import datetime
from os import listdir
from os.path import isfile, join, isdir
from pprint import pprint
import os

def generate_event_list():
    final_path_list = []
    year_list_full = []
    month_list_full = []
    day_list_full = []
    event_list_full = []
    mypath = '/Users/Havens/Documents/GitHub/imgur_api/Photos/'

    year_list = [name for name in listdir(mypath) if isdir(mypath) and name != ".DS_Store"] #finds all years
    for year in year_list: #appends full path
        year_list_full.append(mypath+year+"/")
    for year in  year_list_full: #finds all months
        month_list = [name for name in listdir(year) if isdir(year) and name != ".DS_Store"]
        for month in month_list: #appends full path
            month_list_full.append(year+month+"/")
    for month in month_list_full:
        day_list = [name for name in listdir(month) if isdir(month) and name != ".DS_Store"]
        for day in day_list:
            day_list_full.append(month+day+"/")
    for day in day_list_full:
        event_list = [name for name in listdir(day) if isdir(day) and name != ".DS_Store"]
        for event in event_list:
            event_list_full.append(day+event+"/")
    return event_list_full

final_list = generate_event_list()
for item in final_list:
    #7 - year, 8- month, 9-day, 10- title

    split_item = item.split('/')
    print(item)
    print(split_item[7])
    print(split_item[8])
    print(split_item[9])
    print(split_item[10])
    print(split_item[7]+"/"+split_item[8]+"/"+split_item[9]+" - "+split_item[10])
    print()
#get dates from the event_list_full names
