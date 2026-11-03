"""Flag backgrounds (GM approved 3 Nov 2026). flag_bg('et', out=...) one country; flag_bg('nz','in', out=...) two teams split diagonally with a lime line."""
import base64,numpy as np
from PIL import Image,ImageFilter
from playwright.sync_api import sync_playwright
FL='/home/claude/fonts/node_modules/flag-icons/flags/4x3/'
def _svg(cc,w,h,out):
    d=base64.b64encode(open(FL+cc+'.svg','rb').read()).decode()
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page(viewport={'width':w,'height':h})
        pg.set_content(f"<html><body style='margin:0'><img src='data:image/svg+xml;base64,{d}' style='width:{w}px;height:{h}px;object-fit:cover;display:block'></body></html>")
        pg.screenshot(path=out);b.close()
    return Image.open(out).convert('RGB')
def _wave(img,amp=28,lam=520,shade=.32,ph=0):
    a=np.array(img).astype(float); H,W,_=a.shape; yy,xx=np.mgrid[0:H,0:W]
    t=2*np.pi*(xx+0.35*yy)/lam+ph
    sy=(yy+amp*np.sin(t)).clip(0,H-1).astype(int); sx=(xx+amp*0.4*np.cos(t)).clip(0,W-1).astype(int)
    return Image.fromarray((a[sy,sx]*(1+shade*np.cos(t))[...,None]).clip(0,255).astype('uint8'))
def _finish(img):
    img=img.filter(ImageFilter.GaussianBlur(1.2)); a=np.array(img).astype(float); H,W,_=a.shape; yy,xx=np.mgrid[0:H,0:W]
    v=1-0.55*(((xx-W/2)/(W/1.4))**2+((yy-H*0.4)/(H/1.3))**2)
    return Image.fromarray((a*v.clip(.35,1)[...,None]).clip(0,255).astype('uint8'))
def flag_bg(cc1,cc2=None,out='/tmp/flagbg.jpg'):
    if not cc2:
        f=_svg(cc1,1700,1350,'/tmp/_f1.png').crop((310,0,1390,1350)); _finish(_wave(f,ph=.7)).save(out,quality=92); return out
    a=_wave(_svg(cc1,1500,1350,'/tmp/_f1.png').crop((420,0,1500,1350)),ph=0)
    b=_wave(_svg(cc2,1500,1350,'/tmp/_f2.png').crop((0,0,1080,1350)),ph=1.3)
    H,W=1350,1080; yy,xx=np.mgrid[0:H,0:W]; line=W*0.5+(yy-H/2)*0.35
    o=np.where((xx<line)[...,None],np.array(a),np.array(b)).astype(float); o[np.abs(xx-line)<7]=[200,240,49]
    _finish(Image.fromarray(o.astype('uint8'))).save(out,quality=92); return out
