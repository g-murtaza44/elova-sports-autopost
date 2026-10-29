import sys
from rembg import remove,new_session
from PIL import Image
s=new_session('u2net_human_seg')
for k in sys.argv[1:]:
    im=Image.open(f'/home/claude/commons/{k}.jpg').convert('RGB')
    o=remove(im,session=s,alpha_matting=False)
    bb=o.getbbox(); o=o.crop(bb); o.save(f'/home/claude/commons/{k}_cut.png'); print(k,o.size)
