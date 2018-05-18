#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018  <@DESKTOP-TA60DPH>
#
# Distributed under terms of the MIT license.
# Auther : RB

import requests 

import simplejson as json
import pandas as pd
from simplejson.compat import StringIO
"""
get the ranking between NTU on kaggle competition
"""
rank = requests.get("https://www.kaggle.com/c/8900/leaderboard.json?includeBeforeUser=false&includeAfterUser=true")

io = StringIO(rank.text)
data = json.load(io)
# data = pd.DataFrame.from_dict(io,orient='index')
before = data["beforeUser"]
near = data["nearUser"]
after = data["afterUser"]

counter = 1
print(format("rank","^6"),format('score',"^15"),format('teamName',"<30"))
for i in before:
    if i['teamName'][:4] == "NTU_":
        if i['teamName'] == "NTU_r06942018___":
            position = counter
        print(format(counter,"^6"),format(i['score'],"^15"),format(i['teamName'],"<30"))
        counter+=1
for i in near:
    if i['teamName'][:4] == "NTU_":
        if i['teamName'] == "NTU_r06942018___":
            position = counter
        print(format(counter,"^6"),format(i['score'],"^15"),format(i['teamName'],"<30"))
        counter+=1

for i in after:
    if i['teamName'][:4] == "NTU_":
        if i['teamName'] == "NTU_r06942018___":
            position = counter
        print(format(counter,"^6"),format(i['score'],"^15"),format(i['teamName'],"<30"))
        counter+=1

if position < 10:
    score = 2
if position < 8:
    score = 5
if position < 6:
    score = 7.5 
if position < 4:
    score = 10
print("")
print("Now we are the ",position,"/ 10  in NTU") 
print("the ranking point should be",score)
print("")



