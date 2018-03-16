#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018  <@DESKTOP-TA60DPH>
#
# Distributed under terms of the MIT license.

"""
this program is a crawler program to 
get a movie information from yahoo_movie
"""

import requests 
from bs4 import BeautifulSoup
import simplejson as json
import pandas as pd

'''
data = serializers.serialize("json", OrgInvite.objects.filter(token=100))
'''
res = requests.get("https://movies.yahoo.com.tw/movieinfo_main.html/id=7819")
#print(res.text)
content = BeautifulSoup(res.text,"html.parser")

c6 = len(content.select(".icon_6"))
c12 = len(content.select(".icon_12"))
c15 = len(content.select(".icon_15"))
c18 = len(content.select(".icon_18"))
#default be 普遍級
classification=0
if c6>0:
    classification=1
if c12>0:
    classification=2
if c15>0:
    classification=3
if c18>0:
    classification=4

score = content.select('.score')[0].select('div')[0].text
image = content.select(".movie_intro_foto")[0].select("img")[0].get('src')

info = content.select(".movie_intro_info_r")
name = info[0].select("h1")[0].text
englishname = info[0].select("h3")[0].text
info2 = info[0].select('span')
date = info2[0].text
time = info2[1].text
company = info2[2].text
info3 = content.select(".movie_intro_list")
director = "".join(info3[0].text.split())
actor = "".join(info3[1].text.split())
descri = content.select(".gray_infobox_inner")

object = {'movie':name,'movie_subtitle':englishname,'classification':classification,
    'image_url':image,'date':date,'score':score,'director':director,'actor':actor,'description':descri}

json_df = pd.DataFrame(object)
json_df.to_json('movies.json',orient='records',force_ascii=False,lines=True)

#print(json.dumps(object, separators=(',', ':')))
'''
print(name)#movie
print(englishname)#movie_subtitle
print(classification)#classification
print(image)#image_url
#print(info2)
print(date)
print(score)
print(director)
print(actor)
print(descri)
'''
