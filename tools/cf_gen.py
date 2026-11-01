import os,json,base64,urllib.request
A=os.environ["CF_ACCOUNT_ID"];T=os.environ["CF_API_TOKEN"]
os.makedirs("ai",exist_ok=True);log=open("ai/cf_log.txt","w")
M=[("@cf/leonardo/lucid-origin",{"width":1080,"height":1350,"steps":30}),("@cf/black-forest-labs/flux-1-schnell",{"steps":8})]
for line in open("tools/cf_prompts.txt"):
    if "|" not in line: continue
    k,p=line.strip().split("|",1)
    for m,extra in M:
        try:
            r=urllib.request.Request(f"https://api.cloudflare.com/client/v4/accounts/{A}/ai/run/{m}",data=json.dumps(dict(prompt=p,**extra)).encode(),headers={"Authorization":"Bearer "+T,"Content-Type":"application/json"})
            d=json.loads(urllib.request.urlopen(r,timeout=180).read())
            n=m.split("/")[-1]; open(f"ai/{k}_{n}.jpg","wb").write(base64.b64decode(d["result"]["image"])); log.write(f"{k} {m} ok\n")
        except Exception as e:
            log.write(f"{k} {m} FAIL {(e.read().decode() if hasattr(e,'read') else str(e))[:300]}\n")
log.close()
