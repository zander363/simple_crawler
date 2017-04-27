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
a=urllib.parse.parse_qs(jd["url_encoded_fmt_stream_map"])
#select the file format and resolution
video=requests.get(a['url'][0],stream=True)
#use the youtube name as the default name
name=input("name this video\n")
file=open(name+".mp4",'wb')
#can chage the default location to storage
shutil.copyfileobj(video.raw,file)
#add the status line
file.close()
print('the download is done')

