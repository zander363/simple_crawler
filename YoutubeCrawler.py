#!/usr/bin/env python
import requests
import urllib.parse
from YoutubeAnalysis import YoutubeAnalysis
import shutil
import progressbar

target=input("please input the destination youtube URL\n")
par=YoutubeAnalysis(target)
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
    print(str(i+1)+'.')
    if q:
        print(par['quality'][i])
    if t:
        print(par['type'][i])
select=int(input("which format would you want?\n"))-1
#select the file format and resolution
while(select>len(par['url'])):
    res=requests.get(target)
    tem=res.search('"args":({.*?}),"',res.text)
    jd=json.loads(tem.group(1))
    par=urllib.parse.parse_qs(jd["url_encoded_fmt_stream_map"])
    sleep(1)

video=requests.get(par['url'][select],stream=True)
while(video.status_code!=200):
    video=requests.get(par['url'][select],stream=True)
    sleep(1)
print(video)
#detect the failed donload
#use the youtube name as the default name
name=input("name this video\n")
file=open(name,'wb')
#with open(name,'wb') as f:
#can chage the default location to storage
#    leng=int(video.headers.get('content-length'))
#    for chunk in progressbar.ProgressBar(video.iter_content(chunk_size=1024),expected_size=1+(total_size/1024) ):
#        if chunk:
#            f.write(chunk)
#            f.flush()
shutil.copyfileobj(video.raw,file)
#add the progressbar
file.close()
print('the download is done')

