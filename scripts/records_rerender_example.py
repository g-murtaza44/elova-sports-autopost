import sys; sys.path.insert(0,'/home/claude/enginerepo/v2')
import v2
v2.ICONS=v2.ICONS  # loaded from engine path
from v2 import post,flag
B='/home/claude/enginerepo/v2/bg/'; T='/tmp/rr/'
def ns(num): 
    n=len(num); fs=440 if n<=3 else 330 if n<=5 else 250 if n<=7 else 210
    return f'font-size:{fs}px;left:40px;top:200px'
FULL='right:-10px;top:360px;height:980px'; HALF='right:-30px;bottom:330px;width:540px'
P=[
('2026-11-03-2','athletics','none','56:51',"Yomif Kejelcha Runs The <em>Fastest Half Marathon</em> Ever",'et','ETHIOPIA · BUENOS AIRES · 23 AUG 2026','Representative photo: Mikhail K / Unsplash','WORLD RECORD · ATHLETICS','width:2px'),
('2026-11-04-1','swimming','none','14:26.79',"Johannes Liebmann Takes Down Finke's <em>1500m Free</em> World Record",'de','GERMANY · EUROPEAN CHAMPS · 15 AUG 2026','Representative photo: Thomas Rodriguez / Unsplash','WORLD RECORD · SWIMMING','width:2px'),
('2026-11-04-2','swimming','douglass','23.19',"Kate Douglass Lowers The <em>50m Freestyle</em> World Record",'us','USA · PAN PACIFICS · 15 AUG 2026','Photos: Madie Chandler (CC0), Thomas Rodriguez / Unsplash','WORLD RECORD · SWIMMING',HALF),
('2026-11-05-1','swimming','curtis','26.56',"Sara Curtis Breaks The <em>50m Backstroke</em> World Record Twice",'it','ITALY · EUROPEAN CHAMPS · 13 AUG 2026','Photos: Agnagnas (CC BY-SA 4.0), Thomas Rodriguez / Unsplash','WORLD RECORD · SWIMMING','right:20px;bottom:330px;height:620px'),
('2026-11-05-2','athletics','kerr','3:42.66',"Josh Kerr Breaks El Guerrouj's <em>Mile</em> World Record",'gb','GREAT BRITAIN · LONDON DIAMOND LEAGUE · 18 JUL 2026','Photos: jenaragon94 (CC BY 2.0), Mikhail K / Unsplash','WORLD RECORD · ATHLETICS',FULL),
('2026-11-06-1','athletics','wanyonyi','2:11.83',"Emmanuel Wanyonyi Breaks A <em>27-Year-Old</em> 1000m World Record",'ke','KENYA · MONACO DIAMOND LEAGUE · 10 JUL 2026','Photos: Quejaytee (CC BY-SA 4.0), Mikhail K / Unsplash','WORLD RECORD · ATHLETICS',HALF),
('2026-11-06-2','swimming','none','2:01.65',"Summer McIntosh Breaks A <em>17-Year-Old</em> 200m Fly World Record",'ca','CANADA · 5 JUL 2026','Representative photo: Thomas Rodriguez / Unsplash','WORLD RECORD · SWIMMING','width:2px'),
('2026-11-07-1','athletics','tharp','12.75',"Ja'Kobe Tharp Breaks The <em>110m Hurdles</em> World Record",'us','USA · NCAA CHAMPS, EUGENE · 10 JUN 2026','Photos: youthrunnermag (CC BY 3.0), Mikhail K / Unsplash','WORLD RECORD · ATHLETICS',HALF),
('2026-11-07-2','athletics','duplantis','6.31M',"Mondo Duplantis Raises The <em>Pole Vault</em> World Record Again",'se','SWEDEN · UPPSALA · 12 MAR 2026','Photos: Frankie Fouganthin (CC BY-SA 4.0), Mikhail K / Unsplash','WORLD RECORD · ATHLETICS',HALF),
]
only=sys.argv[1:] 
for d,sp,c,num,hl,cc,meta,cr,tag,cs in P:
    if only and d not in only: continue
    post(B+sp+'.jpg',T+c+'.png',num,hl,f"{flag(cc)} {meta}",cr,tag,f'/tmp/rr/out/{d}.png',cs,ns(num),bgf='brightness(.5) saturate(1.1)')
    print(d)
