import urllib.request as request
import json
from copy import deepcopy
from operator import itemgetter

# get data from url and sorted by id
src1 = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
src2 = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"
with request.urlopen(src1) as response1:
    ch_dataraw = json.load(response1)
ch_data = deepcopy(ch_dataraw)
ch_list = ch_data["list"]
ch_list_sorted = sorted(ch_list, key = itemgetter("_id"))

with request.urlopen(src2) as response2:
    en_dataraw = json.load(response2)
en_data = deepcopy(en_dataraw)
en_list = en_data["list"]
en_list_sorted = sorted(en_list, key = itemgetter("_id"))

# combine two list and write into csv file
with open("hotels.csv", "w", encoding ="utf-8") as file:
    for ch, en in zip(ch_list_sorted, en_list_sorted):
        file.write(
            f'{ch["旅宿名稱"]},{en["hotel name"]}'
            f'{ch["地址"]},{en["address"]}'
            f'{en["tel"]},{en["the total number of rooms"]}\n'
        )

# turn the address into the district only 
for d in ch_list_sorted:
    if isinstance(d["地址"], str):
        d["地址"] = d["地址"][3:6]

# make a new list for counting district and rooms [{"name": area, "count": , "rooms": }]
# compare each data and area(new list)
# if data[distirct] already exsist in area then put data into area and break (outer loop: chnage next data)
# if data[distirct] not exsist in area, create area with data[district]
# first cycle area is empty so inner loop won't execute, found = false, area.append first data
area = []
for d in ch_list_sorted:
    found = False
    for a in area:
        if d["地址"] == a["name"]:
            a["count"] = a["count"] + 1
            a["rooms"] = a["rooms"] + int(d["房間數"])
            found = True
            break
    if found:
        continue
    area.append({"name": (d["地址"]), "count": 1, "rooms": int(d["房間數"])})

with open("district.csv", "w", encoding="utf-8") as file:
    for d in area:
        file.write(f'{d["name"]},{d["count"]},{d["rooms"]}\n')
