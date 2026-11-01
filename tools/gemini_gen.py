import os,json,base64,urllib.request
K=os.environ["GEMINI_API_KEY"];B="https://generativelanguage.googleapis.com/v1beta/"
os.makedirs("ai",exist_ok=True);log=open("ai/gemini_log.txt","w")
def call(u,body=None):
    r=urllib.request.Request(u,data=json.dumps(body).encode() if body else None,headers={"Content-Type":"application/json","x-goog-api-key":K})
    return json.loads(urllib.request.urlopen(r,timeout=180).read())
ms=[m["name"] for m in call(B+"models?pageSize=200")["models"] if "image" in m["name"]]
log.write("image models: %s\n"%ms)
for line in open("tools/gemini_prompts.txt"):
    if "|" not in line: continue
    k,p=line.strip().split("|",1); ok=False
    for m in [x for x in ms if "imagen" not in x]:
        try:
            d=call(B+m+":generateContent",{"contents":[{"parts":[{"text":p}]}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5"}}})
            for part in d["candidates"][0]["content"]["parts"]:
                if "inlineData" in part:
                    open(f"ai/{k}.png","wb").write(base64.b64decode(part["inlineData"]["data"])); ok=True
            log.write(f"{k} {m} ok={ok}\n")
            if ok: break
        except Exception as e:
            msg=e.read().decode()[:300] if hasattr(e,"read") else str(e)
            log.write(f"{k} {m} FAIL {msg}\n")
log.close()
