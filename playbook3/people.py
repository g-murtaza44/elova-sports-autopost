C='/home/claude/commons/'
def credit(t): return f'<div style="position:absolute;right:22px;bottom:150px;z-index:5;writing-mode:vertical-rl;transform:rotate(180deg);font-family:S;font-size:17px;letter-spacing:1px;color:rgba(255,255,255,.75)">Photo: {t}</div>'
def comp(bg,sport,date,num,hl,cut,cr,h=1150,right=-10,top=150,numsize=260,bgfilter='filter:saturate(.6) brightness(.55)',bgpos='center'):
    n=f'<div style="position:absolute;top:170px;left:50px;font-family:H;font-size:{numsize}px;line-height:.9;color:#C8F031;letter-spacing:-6px;z-index:1">{num}</div>' if num else ''
    return f"""<div class="bg">{img(P+bg,bgpos,bgfilter)}</div>
<div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(7,22,14,.55),rgba(10,40,24,.25) 45%,rgba(7,22,14,0) 60%)"></div>
{n}<img src="{pimg(C+cut)}" style="position:absolute;right:{right}px;top:{top}px;height:{h}px;z-index:2;filter:drop-shadow(0 20px 40px rgba(0,0,0,.6))">
<div class="fade" style="z-index:2;height:640px"></div>{head(sport)}
<div class="txt" style="z-index:4"><div class="date">{date}</div><div class="hl">{hl}</div></div>{credit(cr)}{icons}"""
def full(photo,pos,sport,date,num,hl,cr,extra=''):
    bg=f'<img src="{pimg2(C+photo)}" style="width:100%;height:100%;object-fit:cover;object-position:{pos};{extra}">'
    base=bigstat(bg,sport,date,num,hl) if num else cover(bg,sport,date,hl)
    return base.replace(icons,credit(cr)+icons)
def pimg2(f): return 'data:image/jpeg;base64,'+_bb.b64encode(open(f,'rb').read()).decode()
import os
def have(k): return os.path.exists(C+k)
if have('pele.jpg'): posts["2026-11-01-1"]=full('pele.jpg','45% 20%',"FOOTBALL · WORLD CUP","1958 · 1962 · 1970","3","Pelé is still the only player to win <b>three World Cups</b>","public domain (Mexico City, 1970)")
if have('messi_cut.png'): posts["2026-11-03-2"]=comp('goal.jpg',"FOOTBALL · WORLD CUP","18 DECEMBER 2022 · LUSAIL","3-3","Argentina beat <b>France</b> on penalties after a 3-3 thriller to win the <b>World Cup</b>",'messi_cut.png',"Hossein Zohrevand/Tasnim, CC BY 4.0",h=1080,right=20,top=200)
if have('phelps_cut.png'): posts["2026-11-03-1"]=comp('pool.jpg',"SWIMMING · OLYMPICS","2004 TO 2016","23","Michael Phelps won <b>23 Olympic gold medals</b>, the most of any athlete ever",'phelps_cut.png',"Fernando Frazão/Agência Brasil, CC BY 3.0 BR",h=1150,right=-60,top=160,bgfilter='filter:brightness(.6)')
if have('serena.jpg'): posts["2026-11-07-1"]=full('serena_crop.jpg','center',"TENNIS · GRAND SLAMS","1999 TO 2017","23","Serena Williams won <b>23 Grand Slam</b> singles titles, the most of the Open Era","Clavecin, public domain (Wimbledon 2007)")
def panel(photo,sport,date,hl,cr,ph=760,pos='center',num=None,bg='cfield.jpg'):
    n=f'<div style="font-family:H;font-size:200px;color:#C8F031;line-height:1;letter-spacing:-4px">{num}</div>' if num else ''
    return f"""<div class="bg">{img(P+bg,'center','filter:blur(8px) brightness(.35);transform:scale(1.1)')}</div>
<div style="position:absolute;top:130px;left:0;right:0;height:{ph}px;overflow:hidden"><img src="{pimg2(C+photo)}" style="width:100%;height:100%;object-fit:cover;object-position:{pos}"></div>
<div style="position:absolute;top:{130+ph-200}px;left:0;right:0;height:200px;background:linear-gradient(to bottom,rgba(7,22,14,0),#07160E)"></div>
{head(sport)}<div class="txt" style="z-index:4"><div class="date">{date}</div>{n}<div class="hl">{hl}</div></div>{credit(cr)}{icons}"""
from PIL import Image as _I
def flip(src,dst):
    if not have(dst): _I.open(C+src).transpose(_I.FLIP_LEFT_RIGHT).save(C+dst)
posts["2026-11-02-1"]=comp('adelaide.jpg',"CRICKET · TEST","DON BRADMAN · 1928 TO 1948","99.94","Bradman's Test batting average. Nobody has finished a career <b>anywhere near it</b>",'bradman_cut.png',"Sam Hood, CC BY-SA 3.0 AU (c. 1932)",h=980,right=-40,top=400,numsize=220,bgfilter='filter:grayscale(1) brightness(.5)',bgpos='center top')
posts["2026-11-02-3"]=comp('squash.jpg',"SQUASH · RECORDS","1981 TO 1986","555","Pakistan's Jahangir Khan won <b>555 matches in a row</b> without losing",'jahangir_cut.png',"Ian Butterworth, GFDL",h=900,right=-120,top=300,bgfilter='filter:brightness(.5) saturate(.6)')
posts["2026-11-04-1"]=comp('delhi.jpg',"CRICKET · TEST","APRIL 2004 · ANTIGUA","400*","Brian Lara scores <b>400 not out</b> against England, still the highest Test score",'lara_cut.png',"Ukexpat, CC BY-SA 3.0 (Barbados 2002)",h=1000,right=-90,top=290,bgpos='center top')
posts["2026-11-04-2"]=full('sachin.jpg','30% 20%',"CRICKET · RECORDS","16 MARCH 2012 · MIRPUR","100","Sachin Tendulkar becomes the first player to score <b>100 international</b> centuries","Riana, CC BY-SA 4.0 (Adelaide Oval 2008)")
flip('bolt_cut.png','bolt_cut_f.png')
posts["2026-11-06-1"]=comp('track.jpg',"ATHLETICS · 200M","20 AUGUST 2009 · BERLIN","19.19","Four days after his 9.58, Usain Bolt set a <b>200m world record</b> that still stands",'bolt_cut_f.png',"Fernando Frazão/Agência Brasil, CC BY 3.0 BR (Rio 2016)",bgpos='center 75%',h=1000,top=400,numsize=230)
posts["2026-11-06-3"]=comp('cfield.jpg',"CRICKET · RECORDS","22 FEBRUARY 2003 · CAPE TOWN","161.3","km/h. Shoaib Akhtar bowls the <b>fastest ball</b> ever recorded, against England",'shoaib2_cut.png',"Doha Stadium Plus Qatar, CC BY 2.0",h=1080,right=0,top=170,numsize=230)
posts["2026-11-08-1"]=panel('muralib.jpg',"CRICKET · TEST","22 JULY 2010 · GALLE","Muttiah Muralitharan takes his <b>800th Test wicket</b> with his final ball in Tests","Rae Allen, CC BY 2.0 (Murali bowling, 2006)",ph=720,pos='35% center',num="800")
posts["2026-11-08-3"]=panel('dhoni.jpg',"CRICKET · ODI","2 APRIL 2011 · MUMBAI","India beat <b>Sri Lanka</b> by 6 wickets as Dhoni finishes it <b>with a six</b>","Dee03, CC BY-SA 3.0 (Dhoni batting)",ph=760,pos='30% center')
posts["2026-11-01-1"]=full('pele.jpg','40% 15%',"FOOTBALL · WORLD CUP","1958 · 1962 · 1970","3","Pelé is still the only player to win <b>three World Cups</b>","public domain (Mexico City, 1970)")
