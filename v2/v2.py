import base64 as b, sys
from playwright.sync_api import sync_playwright
F='/home/claude/fonts/node_modules/@fontsource/'; FL='/home/claude/fonts/node_modules/flag-icons/flags/4x3/'
def u(p,m): return f"data:{m};base64,{b.b64encode(open(p,'rb').read()).decode()}"
def ff(n,p,w): return f"@font-face{{font-family:'{n}';font-weight:{w};src:url({u(F+p,'font/woff2')})}}"
CSS=ff('H','archivo-black/files/archivo-black-latin-400-normal.woff2',400)+ff('S','barlow-condensed/files/barlow-condensed-latin-700-normal.woff2',700)+ff('S','barlow-condensed/files/barlow-condensed-latin-800-normal.woff2',800)+"""
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1350px;overflow:hidden;background:#06130C;color:#fff;position:relative}
.bg{position:absolute;inset:0;background-size:cover}
.logo{position:absolute;top:48px;left:52px;display:flex;align-items:center;gap:16px;z-index:9}
.logo .m{width:84px;height:84px;border-radius:14px;background:#06130C;border:2px solid rgba(255,255,255,.15);position:relative;color:#fff;font-family:H;font-size:50px;line-height:1;display:flex;justify-content:center;padding-top:10px}.logo .m:after{content:'';position:absolute;left:18px;right:16px;bottom:14px;height:10px;background:#C8F031;transform:skewX(-25deg)}
.logo .t{font-family:H;font-size:44px;line-height:.9}.logo .t span{display:block;font-family:S;font-weight:800;font-size:25px;letter-spacing:9px;color:#C8F031;margin-top:6px}
.tag{position:absolute;top:66px;right:52px;font-family:S;font-weight:800;font-size:26px;letter-spacing:4px;background:rgba(0,0,0,.55);border:2px solid #C8F031;padding:10px 20px;border-radius:40px;z-index:9}
.hl{position:absolute;left:56px;right:56px;bottom:170px;font-family:H;font-size:70px;line-height:1.08;text-shadow:0 4px 24px rgba(0,0,0,.6);z-index:8}
.hl em{font-style:normal;color:#C8F031}
.meta{position:absolute;left:56px;bottom:92px;font-family:S;font-weight:800;font-size:31px;letter-spacing:3px;display:flex;align-items:center;gap:14px;z-index:8}
.meta img{height:34px;width:45px;border-radius:5px}
.cr{position:absolute;right:30px;bottom:24px;font-family:S;font-weight:700;font-size:18px;opacity:.7;z-index:8}
.ic{position:absolute;left:56px;bottom:34px;font-family:S;font-weight:800;font-size:24px;letter-spacing:2px;color:#C8F031;z-index:8}
"""
def flag(cc): return f'<img src="{u(FL+cc+".svg","image/svg+xml")}">'
def post(bg,cut,num,hl,meta,cr,tag,out,cutstyle,numstyle,bgf='brightness(.55)'):
    h=f"""<div class="bg" style="background-image:url({u(bg,'image/jpeg')});filter:{bgf}"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 60% 35%,rgba(200,240,49,.18),transparent 60%)"></div>
<div style="position:absolute;{numstyle};font-family:H;color:#C8F031;line-height:.8;letter-spacing:-12px;text-shadow:0 10px 60px rgba(0,0,0,.5)">{num}</div>
<img src="{u(cut,'image/png')}" style="position:absolute;{cutstyle};filter:brightness(.92) contrast(1.12) saturate(1.05) drop-shadow(-3px 0 2px rgba(200,240,49,.55)) drop-shadow(0 0 30px rgba(0,0,0,.7))">
<div style="position:absolute;left:0;right:0;bottom:0;height:720px;background:linear-gradient(transparent,rgba(6,19,12,.85) 40%,#06130C 78%)"></div>
<div style="position:absolute;inset:0;opacity:.13;mix-blend-mode:overlay;background-image:url(&quot;data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>&quot;);z-index:7"></div><div class="logo"><div class="m">E</div><div class="t">ELOVA<span>SPORTS</span></div></div><div class="tag">{tag}</div>
<div class="hl">{hl}</div><div class="meta">{meta}</div><div class="ic">@ELOVASPORTS</div><div class="cr">{cr}</div>"""
    with sync_playwright() as p:
        br=p.chromium.launch();pg=br.new_page(viewport={'width':1080,'height':1350})
        pg.set_content(f"<html><head><style>{CSS}</style></head><body>{h}</body></html>");pg.wait_for_timeout(300);pg.screenshot(path=out);br.close()
if __name__=='__main__':
    S='/home/claude/enginerepo/v2/';C='/home/claude/commons/'
    post(S+'stadium_crowd.jpg','/home/claude/enginerepo/commons/brook_v2.png','202',
     "Harry Brook Hits England's First ODI <em>Double Hundred</em>, And Still Loses",
     f"{flag('gb-eng')} ENGLAND <span style='color:#C8F031'>V</span> SRI LANKA {flag('lk')}",
     "Photos: Dave Morton (PD), Damien Tait / Unsplash","CRICKET · ODI",'/tmp/sample-brook.png',
     'height:1100px;right:-45px;top:110px','font-size:440px;left:30px;top:270px',bgf='brightness(.42) saturate(1.2) contrast(1.1)')
