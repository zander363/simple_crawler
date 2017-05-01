def YoutubeAnalysis(URL):
    import requests
    import re
    import json
    import urllib.parse
    res=requests.get(URL)
    tem=re.search('"args":({.*?}),"',res.text)
    jd=json.loads(tem.group(1))
    par=urllib.parse.parse_qs(jd["url_encoded_fmt_stream_map"])
    return par
    
