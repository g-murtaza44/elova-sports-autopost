import urllib.request,urllib.parse,os,time
os.makedirs("ai",exist_ok=True)
for line in open("tools/ai_prompts.txt"):
    if "|" not in line: continue
    k,p=line.strip().split("|",1)
    u="https://image.pollinations.ai/prompt/"+urllib.parse.quote(p)+"?width=1080&height=1350&nologo=true&model=flux&seed=7"
    for a in range(4):
        try:
            d=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"ElovaSports/1.0"}),timeout=180).read()
            open(f"ai/{k}.jpg","wb").write(d); print(k,len(d)); break
        except Exception as e: print("retry",e); time.sleep(15)
