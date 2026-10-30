import os,urllib.request
from rembg import new_session,remove
from PIL import Image
os.makedirs('cut',exist_ok=True)
M=['birefnet-portrait','birefnet-general']
jobs=[l.split() for l in open('tools/cut_list.txt') if l.strip() and not l.startswith('#')]
for m in M:
    s=new_session(m)
    for name,url in jobs:
        src=f'/tmp/{name}'
        if not os.path.exists(src):
            urllib.request.urlretrieve(urllib.request.Request(url,headers={'User-Agent':'ElovaBot/1.0'}).full_url,src)
        im=Image.open(src).convert('RGB')
        remove(im,session=s,post_process_mask=True).save(f'cut/{os.path.splitext(name)[0]}_{m}.png'); print(m,name)
