import os,traceback,urllib.request,urllib.parse,time
os.makedirs("ai",exist_ok=True);L=open("ai/hf_log.txt","w")
from gradio_client import Client
for s in ["yanze/PuLID-FLUX","ByteDance/InfiniteYou-FLUX","InstantX/InstantID","multimodalart/Ip-Adapter-FaceID","Kwai-Kolors/Kolors-FaceID","guoyww/PhotoMaker-V2","TencentARC/PhotoMaker-V2"]:
    try:
        c=Client(s,verbose=False); L.write(f"=== {s}\n{c.view_api(print_info=False,return_format='str')}\n")
    except Exception as e: L.write(f"=== {s} FAIL {str(e)[:300]}\n")
    L.flush()
R="https://raw.githubusercontent.com/g-murtaza44/elova-sports-autopost/assets/refs/rohail_ref.jpg"
p="Photorealistic sports agency photo of this exact man (same face, curly hair, beard), Pakistan cricketer in light green Pakistan Shaheens kit, raising his bat after an unbeaten fifty, walking off under floodlights in a real international cricket stadium with crowd and Pakistan flags, vertical"
for m in ["kontext","gptimage","nanobanana","seedream"]:
    u="https://image.pollinations.ai/prompt/"+urllib.parse.quote(p)+f"?model={m}&image={urllib.parse.quote(R,safe='')}&width=1080&height=1350&nologo=true&seed=7"
    try:
        d=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"ElovaSports/1.0"}),timeout=240).read()
        open(f"ai/poll_{m}.jpg","wb").write(d); L.write(f"poll {m} ok {len(d)}\n")
    except Exception as e: L.write(f"poll {m} FAIL {(e.read().decode()[:200] if hasattr(e,'read') else str(e))}\n")
    L.flush()
L.close()
