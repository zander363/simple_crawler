#!/usr/bin/env python
import requests
import re
import json
import urllib.parse
import shutil
target=input("please input the destination youtube URL\n")
res=requests.get(target)
tem=re.search('"args":({.*?}),"',res.text)
jd=json.loads(tem.group(1))
par=urllib.parse.parse_qs(jd["url_encoded_fmt_stream_map"])
q=False
t=False
if len(par['quality'])>=5:
    q=True
if len(par['type'])>=2:
    t=True
times=len(par['quality'])
if times<len(par['type']):
    times=len(par['type'])
for i in range(times): 
    print(str(i+1)+'.  ')
    if q:
        print(par['quality'][i])
    if t:
        print(par['type'][i])
select=int(input("which format would you want?\n"))-1
#select the file format and resolution
video=requests.get(par['url'][select],stream=True)
#use the youtube name as the default name
name=input("name this video\n")
file=open(name+".mp4",'wb')
#can chage the default location to storage
shutil.copyfileobj(video.raw,file)
#add the status line
file.close()
print('the download is done')

