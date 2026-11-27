import os,json,base64,urllib.request
A=os.environ["CF_ACCOUNT_ID"];T=os.environ["CF_API_TOKEN"]
os.makedirs("ai",exist_ok=True);log=open("ai/cf_log.txt","w")
# Default: flux-1-schnell only (cheap, ~3-5 images/day fit in the free 10k neurons).
# Use "key@lucid|prompt" to spend the day's quota on one Lucid Origin image instead.
FLUX=("@cf/black-forest-labs/flux-1-schnell",{"steps":8})
LUCID=("@cf/leonardo/lucid-origin",{"width":1080,"height":1350,"steps":30})
for line in open("tools/cf_prompts.txt"):
    if "|" not in line: continue
    k,p=line.strip().split("|",1)
    M=[LUCID] if k.endswith("@lucid") else [FLUX]; k=k.replace("@lucid","")
    for m,extra in M:
        try:
            r=urllib.request.Request(f"https://api.cloudflare.com/client/v4/accounts/{A}/ai/run/{m}",data=json.dumps(dict(prompt=p,**extra)).encode(),headers={"Authorization":"Bearer "+T,"Content-Type":"application/json"})
            d=json.loads(urllib.request.urlopen(r,timeout=180).read())
            n=m.split("/")[-1]; open(f"ai/{k}_{n}.jpg","wb").write(base64.b64decode(d["result"]["image"])); log.write(f"{k} {m} ok\n")
        except Exception as e:
            log.write(f"{k} {m} FAIL {(e.read().decode() if hasattr(e,'read') else str(e))[:300]}\n")
log.close()
