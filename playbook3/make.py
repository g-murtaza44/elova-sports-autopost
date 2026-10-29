from playwright.sync_api import sync_playwright
import base64
img=lambda f,pos='center top',extra='':f'<img src="data:image/jpeg;base64,{base64.b64encode(open(f,"rb").read()).decode()}" style="position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover;object-position:{pos};{extra}">'
BB=img('/home/claude/photos/baseball_b.jpg','center 20%')
BBD=img('/home/claude/photos/baseball_b.jpg','center 20%','filter:blur(6px) brightness(.35);transform:scale(1.05)')
TN=img('/home/claude/photos/tennis_a.jpg','center center','filter:grayscale(.85) brightness(.7)')
NAVY="#07160E"; LIME="#C8F031"; W="#FFFFFF"
css=eval('f"""'+open('css.txt').read()+'"""')
icons='<div class="icons"><span><svg viewBox="0 0 24 24" width="32" height="32"><path d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z" fill="#000"/></svg></span><span><svg viewBox="0 0 24 24" width="32" height="32"><path d="M7.0301.084c-1.2768.0602-2.1487.264-2.911.5634-.7888.3075-1.4575.72-2.1228 1.3877-.6652.6677-1.075 1.3368-1.3802 2.127-.2954.7638-.4956 1.6365-.552 2.914-.0564 1.2775-.0689 1.6882-.0626 4.947.0062 3.2586.0206 3.6671.0825 4.9473.061 1.2765.264 2.1482.5635 2.9107.308.7889.72 1.4573 1.388 2.1228.6679.6655 1.3365 1.0743 2.1285 1.38.7632.295 1.6361.4961 2.9134.552 1.2773.056 1.6884.069 4.9462.0627 3.2578-.0062 3.668-.0207 4.9478-.0814 1.28-.0607 2.147-.2652 2.9098-.5633.7889-.3086 1.4578-.72 2.1228-1.3881.665-.6682 1.0745-1.3378 1.3795-2.1284.2957-.7632.4966-1.636.552-2.9124.056-1.2809.0692-1.6898.063-4.948-.0063-3.2583-.021-3.6668-.0817-4.9465-.0607-1.2797-.264-2.1487-.5633-2.9117-.3084-.7889-.72-1.4568-1.3876-2.1228C21.2982 1.33 20.628.9208 19.8378.6165 19.074.321 18.2017.1197 16.9244.0645 15.6471.0093 15.236-.005 11.977.0014 8.718.0076 8.31.0215 7.0301.0839m.1402 21.6932c-1.17-.0509-1.8053-.2453-2.2287-.408-.5606-.216-.96-.4771-1.3819-.895-.422-.4178-.6811-.8186-.9-1.378-.1644-.4234-.3624-1.058-.4171-2.228-.0595-1.2645-.072-1.6442-.079-4.848-.007-3.2037.0053-3.583.0607-4.848.05-1.169.2456-1.805.408-2.2282.216-.5613.4762-.96.895-1.3816.4188-.4217.8184-.6814 1.3783-.9003.423-.1651 1.0575-.3614 2.227-.4171 1.2655-.06 1.6447-.072 4.848-.079 3.2033-.007 3.5835.005 4.8495.0608 1.169.0508 1.8053.2445 2.228.408.5608.216.96.4754 1.3816.895.4217.4194.6816.8176.9005 1.3787.1653.4217.3617 1.056.4169 2.2263.0602 1.2655.0739 1.645.0796 4.848.0058 3.203-.0055 3.5834-.061 4.848-.051 1.17-.245 1.8055-.408 2.2294-.216.5604-.4763.96-.8954 1.3814-.419.4215-.8181.6811-1.3783.9-.4224.1649-1.0577.3617-2.2262.4174-1.2656.0595-1.6448.072-4.8493.079-3.2045.007-3.5825-.006-4.848-.0608M16.953 5.5864A1.44 1.44 0 1 0 18.39 4.144a1.44 1.44 0 0 0-1.437 1.4424M5.8385 12.012c.0067 3.4032 2.7706 6.1557 6.173 6.1493 3.4026-.0065 6.157-2.7701 6.1506-6.1733-.0065-3.4032-2.771-6.1565-6.174-6.1498-3.403.0067-6.156 2.771-6.1496 6.1738M8 12.0077a4 4 0 1 1 4.008 3.9921A3.9996 3.9996 0 0 1 8 12.0077" fill="#000"/></svg></span><span><svg viewBox="0 0 24 24" width="32" height="32"><path d="M14.234 10.162 22.977 0h-2.072l-7.591 8.824L7.251 0H.258l9.168 13.343L.258 24H2.33l8.016-9.318L16.749 24h6.993zm-2.837 3.299-.929-1.329L3.076 1.56h3.182l5.965 8.532.929 1.329 7.754 11.09h-3.182z" fill="#000"/></svg></span><span style="font-family:H;font-size:22px;color:#000;letter-spacing:-0.5px">in</span></div>'
head=lambda sport:f'<div class="logo"><i></i>ELOVA<span style="font-weight:800;font-size:.8em;letter-spacing:4px;margin-left:12px;color:#C8F031">SPORTS</span></div><div class="sport">{sport}</div>'
defs='<defs><radialGradient id="gl"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".25" stop-color="#EAF6FF" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0B1830"/><stop offset="1" stop-color="#1A3150"/></linearGradient></defs>'
lights="".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#gl)"/>' for x,y,r in [(120,110,170),(540,60,200),(960,110,170)])
crowd='<rect x="0" y="300" width="1080" height="170" fill="#0A1426"/>'+"".join(f'<circle cx="{(i*41)%1080}" cy="{312+(i*57)%150}" r="7" fill="{["#22345A","#2C4470","#1B2A48"][i%3]}"/>' for i in range(220))
# baseball diamond
base=f'''<svg width="1080" height="1350">{defs}<rect width="1080" height="1350" fill="url(#sky)"/>{lights}{crowd}
<rect x="0" y="470" width="1080" height="880" fill="#1F6B3A"/>
{"".join(f'<rect x="0" y="{470+i*70}" width="1080" height="35" fill="#237844"/>' for i in range(13))}
<path d="M540 520 L960 860 L540 1260 L120 860 Z" fill="#B07A4A"/>
<path d="M540 640 L830 870 L540 1110 L250 870 Z" fill="#1F6B3A"/>
<circle cx="540" cy="880" r="55" fill="#B07A4A"/><rect x="525" y="872" width="30" height="8" fill="#fff"/>
<line x1="540" y1="1260" x2="0" y2="720" stroke="#fff" stroke-width="5"/><line x1="540" y1="1260" x2="1080" y2="720" stroke="#fff" stroke-width="5"/>
{"".join(f'<rect x="{x-18}" y="{y-18}" width="36" height="36" fill="#fff" transform="rotate(45 {x} {y})"/>' for x,y in [(540,640),(830,870),(250,870)])}
<polygon points="525,1230 555,1230 555,1250 540,1262 525,1250" fill="#fff"/></svg>'''
# tennis blue court perspective
tennis=f'''<svg width="1080" height="1350">{defs}<rect width="1080" height="1350" fill="#060C18"/>{lights}{crowd.replace("#0A1426","#070E1C")}
<polygon points="0,470 1080,470 1080,1350 0,1350" fill="#0E2A5A"/>
<polygon points="300,500 780,500 1010,1350 70,1350" fill="#1E56B8"/>
<g stroke="#fff" stroke-width="6" fill="none"><polygon points="300,500 780,500 1010,1350 70,1350"/>
<line x1="350" y1="500" x2="165" y2="1350"/><line x1="730" y1="500" x2="915" y2="1350"/>
<line x1="340" y1="640" x2="740" y2="640"/><line x1="540" y1="640" x2="540" y2="1120"/><line x1="250" y1="1120" x2="830" y2="1120"/></g>
<rect x="40" y="840" width="1000" height="16" fill="#E9EEF5"/><g stroke="#C9D3E0" stroke-width="2">{"".join(f'<line x1="{40+i*20}" y1="856" x2="{40+i*20}" y2="905"/>' for i in range(51))}</g>
<line x1="40" y1="905" x2="1040" y2="905" stroke="#C9D3E0" stroke-width="3"/>
<circle cx="760" cy="760" r="16" fill="{LIME}"/></svg>'''
def cover(bg,sport,date,hl,swipe=False):
    return f'<div class="bg">{bg}</div><div class="fade"></div>{head(sport)}<div class="txt"><div class="date">{date}</div><div class="hl">{hl}</div></div>{icons}'+('<div class="swipe">SWIPE ›</div>' if swipe else '')
posts={}
posts["4a-world-series-cover"]=cover(BB,"BASEBALL · MLB","28 OCTOBER 2026 · ST. PETERSBURG, FLORIDA","The <b>Milwaukee Brewers</b> beat the Tampa Bay Rays to win their <b>first-ever World Series</b>")
mom=[("5⅔","scoreless innings","Ace <b>Jacob Misiorowski</b> allowed just two hits in Game 5"),("2","hits, 2 RBI","Rookie <b>Cooper Pratt</b> drove in the first run of the night"),(".381","batting average","Catcher <b>William Contreras</b> hit an RBI double and was named <b>World Series MVP</b>")]
rows="".join(f'<div style="display:flex;gap:30px;align-items:center;background:#123322;border-left:12px solid {LIME};border-radius:12px;padding:30px 36px"><div style="min-width:210px;text-align:center"><div class="hl" style="font-size:84px;color:{LIME};line-height:1">{n}</div><div style="font-weight:800;font-size:24px;letter-spacing:2px;margin-top:8px">{u.upper()}</div></div><div class="hl" style="font-size:38px;line-height:1.25;text-align:left">{t}</div></div>' for n,u,t in mom)
posts["4b-world-series-moments"]=f'''<div class="bg">{BBD}</div>{head("BASEBALL · MLB")}<div style="position:absolute;top:150px;left:60px;right:60px"><div class="hl" style="text-align:center;font-size:70px">3 moments that won it</div>
<div style="display:flex;flex-direction:column;gap:26px;margin-top:50px">{rows}</div>
<div class="hl" style="text-align:center;font-size:44px;margin-top:48px">Game 5: Brewers <b>4</b>, Rays <b>1</b>. Series won <b>4-1</b>.</div></div>{icons}'''
lead=[("7","Novak Djokovic","2008 · 2012 · 2013 · 2014 · 2015 · 2022 · 2023"),("6","Roger Federer","2003 · 2004 · 2006 · 2007 · 2010 · 2011"),("5","Pete Sampras","1991 · 1994 · 1996 · 1997 · 1999"),("5","Ivan Lendl","1981 · 1982 · 1985 · 1986 · 1987")]
lr="".join(f'<div style="display:flex;align-items:center;gap:30px;background:rgba(7,22,14,.82);border-radius:12px;padding:22px 30px"><div class="hl" style="font-size:80px;color:{LIME};width:70px;text-align:center;line-height:1">{n}</div><div style="text-align:left"><div class="hl" style="font-size:44px;line-height:1.1">{p}</div><div style="font-weight:700;font-size:23px;letter-spacing:1px;margin-top:6px">{y}</div></div></div>' for n,p,y in lead)
posts["5-atp-finals-hook"]=f'''<div class="bg">{TN}</div><div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(7,22,14,.6),rgba(10,40,24,.45) 40%,rgba(7,22,14,.92) 85%)"></div>{head("TENNIS · ATP FINALS")}
<div style="position:absolute;top:150px;left:60px;right:60px;text-align:center"><div class="date">TURIN · 15 TO 22 NOVEMBER</div>
<div class="hl" style="font-size:72px">Most <b>ATP Finals</b> titles of all time</div>
<div style="display:flex;flex-direction:column;gap:16px;margin-top:44px">{lr}</div>
<div class="hl" style="font-size:42px;margin-top:40px">Champion in 2024 and 2025, <b>Jannik Sinner</b> now goes for three in a row</div></div>{icons}'''

P='/home/claude/photos/'
def bigstat(bg,sport,date,num,hl):
    return f'<div class="bg">{bg}</div><div class="fade"></div>{head(sport)}<div class="txt"><div class="date">{date}</div><div style="font-family:H;font-size:250px;color:#C8F031;line-height:1;letter-spacing:-4px">{num}</div><div class="hl" style="margin-top:20px">{hl}</div></div>{icons}'
posts["g-bolt"]=bigstat(img(P+'track.jpg','center 70%'),"ATHLETICS · 100M","16 AUGUST 2009 · BERLIN","9.58","Usain Bolt beats <b>Tyson Gay</b> to set a 100m world record that still stands")
posts["g-aus2023"]=cover(img(P+'delhi.jpg','center top'),"CRICKET · ODI","19 NOVEMBER 2023 · AHMEDABAD","Australia beat <b>India</b> by 6 wickets to win a record <b>6th World Cup</b>")
posts["g-offside"]=cover(img(P+'pitch.jpg','center center'),"FOOTBALL · RULES","RULES EXPLAINED","What actually makes a player <b>offside</b>?",swipe=True)
posts["g-pak1992"]=cover(img(P+'adelaide.jpg','center top'),"CRICKET · ODI","25 MARCH 1992 · MELBOURNE","Imran Khan's Pakistan beat <b>England</b> by 22 runs to win their <b>first World Cup</b>")
posts["g-sachin"]=bigstat(img(P+'ball.jpg','center 85%','transform:scale(1.0) translateY(-180px)'),"CRICKET · RECORDS","16 MARCH 2012 · MIRPUR","100","Sachin Tendulkar becomes the first player to score <b>100 international</b> centuries")
posts["g-messi2022"]=cover(img(P+'goal.jpg','center center'),"FOOTBALL · WORLD CUP","18 DECEMBER 2022 · LUSAIL","Argentina beat <b>France</b> on penalties after a 3-3 thriller to win the <b>World Cup</b>")
win=[("1975","West Indies","Australia"),("1979","West Indies","England"),("1983","India","West Indies"),("1987","Australia","England"),("1992","Pakistan","England"),("1996","Sri Lanka","Australia"),("1999","Australia","Pakistan"),("2003","Australia","India"),("2007","Australia","Sri Lanka"),("2011","India","Sri Lanka"),("2015","Australia","New Zealand"),("2019","England","New Zealand"),("2023","Australia","India")]
tr="".join(f'<div style="display:grid;grid-template-columns:110px 1fr 90px 1fr;align-items:center;padding:9px 26px;border-radius:8px;background:{"#2A4A14" if w=="Australia" else "rgba(18,51,34,.88)"};font-size:28px;font-weight:800"><span style="color:#C8F031">{y}</span><span>{w}</span><span style="font-size:22px;text-align:center">BEAT</span><span>{l}</span></div>' for y,w,l in win)
posts["g-odi-list"]=f"""<div class="bg">{img(P+'adelaide.jpg','center top','filter:blur(5px) brightness(.4);transform:scale(1.05)')}</div>{head("CRICKET · ODI")}<div style="position:absolute;top:140px;left:60px;right:60px"><div class="hl" style="text-align:center;font-size:56px">Every <b>ODI World Cup</b> final</div><div style="display:flex;flex-direction:column;gap:7px;margin-top:30px">{tr}</div><div class="hl" style="text-align:center;font-size:40px;margin-top:24px">Australia: <b>6 titles</b>. Who wins in 2027?</div></div>{icons}"""

import base64 as _bb
def pimg(f): return 'data:image/png;base64,'+_bb.b64encode(open(f,'rb').read()).decode()
posts["c-bolt-composite"]=f"""<div class="bg">{img(P+'track.jpg','center 75%','filter:saturate(.6) brightness(.55)')}</div>
<div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(7,22,14,.55),rgba(10,40,24,.25) 45%,rgba(7,22,14,0) 60%)"></div>
<div style="position:absolute;top:170px;left:50px;font-family:H;font-size:260px;line-height:.9;color:#C8F031;letter-spacing:-6px;z-index:1;opacity:.95">9.58</div>
<img src="{pimg('/home/claude/commons/bolt_cut.png')}" style="position:absolute;right:-10px;top:150px;height:1150px;z-index:2;filter:drop-shadow(0 20px 40px rgba(0,0,0,.6))">
<div class="fade" style="z-index:2;height:640px"></div>
{head("ATHLETICS · 100M")}
<div class="txt" style="z-index:4"><div class="date">16 AUGUST 2009 · BERLIN</div><div class="hl">Usain Bolt beats <b>Tyson Gay</b> to set a 100m world record that still stands</div></div>
<div style="position:absolute;right:22px;bottom:150px;z-index:5;writing-mode:vertical-rl;transform:rotate(180deg);font-family:S;font-size:17px;letter-spacing:1px;color:rgba(255,255,255,.75)">Photo: Fernando Frazão/Agência Brasil, CC BY 3.0 BR (Rio 2016)</div>
{icons}"""

exec(open('/home/claude/playbook3/batch1.py').read())
exec(open('/home/claude/playbook3/people.py').read())
import os as _o
if _o.environ.get('BATCH'): exec(open('/home/claude/playbook3/'+_o.environ['BATCH']+'.py').read())
import os,base64 as _b
FS=os.environ.get('FONTSET','')
OUT=os.environ.get('OUT','.')
F='/home/claude/fonts/node_modules/@fontsource/'
def ff(name,path,w):
    return "@font-face{font-family:'%s';font-weight:%s;src:url(data:font/woff2;base64,%s) format('woff2')}"%(name,w,_b.b64encode(open(F+path,'rb').read()).decode())
SETS={
 'anton':(ff('H','anton/files/anton-latin-400-normal.woff2',400),"'H'",400,'1px',1.18),
 'bebas':(ff('H','bebas-neue/files/bebas-neue-latin-400-normal.woff2',400),"'H'",400,'1px',1.05),
 'oswald':(ff('H','oswald/files/oswald-latin-700-normal.woff2',700),"'H'",700,'0px',1.16),
 'teko':(ff('H','teko/files/teko-latin-600-normal.woff2',600),"'H'",600,'0.5px',0.98),
 'league':(ff('H','league-gothic/files/league-gothic-latin-400-normal.woff2',400),"'H'",400,'1px',1.05),
 'saira':(ff('H','saira-extra-condensed/files/saira-extra-condensed-latin-900-normal.woff2',900),"'H'",900,'0.5px',1.14),
 'archivo':(ff('H','archivo-black/files/archivo-black-latin-400-normal.woff2',400),"'H'",400,'0px',1.14),
 'bigshoulders':(ff('H','big-shoulders-display/files/big-shoulders-display-latin-900-normal.woff2',900),"'H'",900,'0.5px',1.05),
}
extra=''
if FS:
    face,fam,wt,ls,lh=SETS[FS]
    sub=ff('S','barlow-condensed/files/barlow-condensed-latin-700-normal.woff2',700)+ff('S','barlow-condensed/files/barlow-condensed-latin-800-normal.woff2',800)
    extra='<style>'+face+sub+'body,.date,.logo,.sport,.swipe{font-family:S!important}.icons span{background:#fff!important;width:54px!important;height:54px!important}'+'.date{font-size:34px!important;letter-spacing:3px}.sport{font-size:27px!important}.logo{font-size:34px!important}'+'.hl{font-family:%s!important;font-weight:%s!important;text-transform:uppercase;letter-spacing:%s;line-height:%s!important}.hl b{font-weight:%s!important;padding:0 10px}'%(fam,wt,ls,lh,wt)+'.hl{text-wrap:balance}.hl b{white-space:nowrap}'+'.hl[style*="font-size:38px"],.hl[style*="font-size:42px"],.hl[style*="font-size:44px"]{font-family:S!important;font-weight:800!important;text-transform:none!important;letter-spacing:0!important;line-height:1.2!important}.hl[style*="font-size:38px"]{font-size:44px!important}.hl[style*="font-size:42px"],.hl[style*="font-size:44px"]{font-size:50px!important}.hl[style*="font-size:44px"] b,.hl[style*="font-size:42px"] b,.hl[style*="font-size:38px"] b{font-weight:800!important}'+'</style>'
    SZ={'bebas':90,'bigshoulders':90,'teko':96,'league':98,'saira':92,'archivo':60,'oswald':74}
    if FS in SZ: extra+='<style>.txt .hl{font-size:%dpx!important}</style>'%SZ[FS]
    if FS=='archivo': extra+='<style>.hl[style*="font-size:70px"],.hl[style*="font-size:72px"]{font-size:58px!important}</style>'
css=css+extra
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    for k,h in posts.items():
        pg.set_content("<html><head>"+css+"</head><body>"+h+"</body></html>"); pg.wait_for_timeout(200); pg.screenshot(path=f"{OUT}/{k}.png")
    b.close()
