from datetime import datetime
from os import listdir
from os.path import isfile, join, isdir
from pprint import pprint

final_path_list = []
year_list_full = []
month_list_full = []
day_list_full = []
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

pprint(day_list_full)



# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# image_list = []
# image_ids = []
# for x in onlyfiles:
#     image_list.append(mypath+x)
