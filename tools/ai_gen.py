import urllib.request,urllib.parse,os,time
# line format: key|prompt  -> writes ai/key_s1.jpg .. ai/key_s3.jpg (3 seeds, pick the best)
os.makedirs("ai",exist_ok=True)
for line in open("tools/ai_prompts.txt"):
    if "|" not in line: continue
    k,p=line.strip().split("|",1)
    for i,seed in enumerate([11,23,37],1):
        u="https://image.pollinations.ai/prompt/"+urllib.parse.quote(p)+f"?width=1080&height=1350&nologo=true&model=flux&enhance=true&seed={seed}"
        for a in range(4):
            try:
                d=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"ElovaSports/1.0"}),timeout=180).read()
                open(f"ai/{k}_s{i}.jpg","wb").write(d); print(k,i,len(d)); break
            except Exception as e: print("retry",e); time.sleep(15)
        time.sleep(5)
