import os,shutil,traceback
from gradio_client import Client, handle_file
os.makedirs("ai",exist_ok=True);L=open("ai/hf_log.txt","w")
NEG="painting, illustration, cartoon, cgi, 3d render, blurry, deformed face, extra fingers, text, watermark, logo"
def save(r,k):
    if isinstance(r,(list,tuple)): r=r[0]
    if isinstance(r,list): r=r[0]
    if isinstance(r,dict): r=r.get("image",r); r=r.get("path",r) if isinstance(r,dict) else r
    shutil.copy(r,f"ai/{k}"+os.path.splitext(r)[1]); return r
for line in open("tools/hf_jobs.txt"):
    if "|" not in line: continue
    k,ref,p=line.strip().split("|",2)
    for name,fn in [
      ("pulid",lambda: Client("yanze/PuLID-FLUX",verbose=False).predict(p,handle_file(ref),0,4,"7",1,896,1152,20,1,NEG,1,128,api_name="/generate_image")),
      #("photomaker",lambda: Client("TencentARC/PhotoMaker-V2",verbose=False).predict([handle_file(ref)],p.replace("this man","man img"),NEG,"35mm film / Portrait (2:3)","Photographic (Default)",40,20,1,5,7,False,{"background":None,"layers":[],"composite":None,"id":None},0.7,0.8,api_name="/generate_image")),
      #("instantid",lambda: Client("InstantX/InstantID",verbose=False).predict(handle_file(ref),None,p,NEG,"(No style)",30,0.8,0.8,0.4,0.4,["depth"],5,7,"EulerDiscreteScheduler",False,True,api_name="/generate_image")),
    ]:
        try: r=fn(); save(r,f"{k}_{name}"); L.write(f"{k} {name} ok\n")
        except Exception as e: L.write(f"{k} {name} FAIL {str(e)[:300]}\n")
        L.flush()
L.close()
