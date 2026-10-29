import json,sys,time,os,re,urllib.request,urllib.parse
UA="ElovaSportsBot/1.0 (ghulammurtaza.wa@gmail.com)"
def get(u):
    for a in range(5):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=60).read()
        except Exception as e: print("retry",e); time.sleep(10*(a+1))
qs=[l.strip() for l in open("tools/queries.txt") if l.strip()]
os.makedirs("found",exist_ok=True); out={}
for q in qs:
    key=re.sub(r'[^a-z0-9]+','_',q.lower())[:40]
    p={"action":"query","generator":"search","gsrsearch":q+" filetype:bitmap","gsrnamespace":"6","gsrlimit":"8","prop":"imageinfo","iiprop":"url|size|extmetadata","iiurlwidth":"960","iiextmetadatafilter":"Artist|LicenseShortName|DateTimeOriginal|ImageDescription","format":"json"}
    d=json.loads(get("https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode(p)))
    res=[]
    for pg in sorted(d.get("query",{}).get("pages",{}).values(),key=lambda x:x.get("index",99)):
        ii=pg["imageinfo"][0];m=ii.get("extmetadata",{})
        g=lambda k:re.sub('<[^>]+>','',m.get(k,{}).get("value",""))[:120]
        res.append(dict(title=pg["title"],w=ii["width"],h=ii["height"],thumb=ii.get("thumburl"),lic=g("LicenseShortName"),artist=g("Artist"),date=g("DateTimeOriginal"),desc=g("ImageDescription")))
    out[key]=res
    for i,r in enumerate(res[:5]):
        if r["thumb"]:
            open(f"found/{key}_{i}.jpg","wb").write(get(r["thumb"])); time.sleep(1)
    time.sleep(2)
json.dump(out,open("found/index.json","w"),indent=1)
