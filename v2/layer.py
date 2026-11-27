# LAYERED STYLE (GM locked 27 Nov 2026): AI player as a dim green duotone back layer,
# giant lime number placed OVER the player's face so viewers read the number and story, not the face.
import cv2, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from v2 import post
DUO = 'grayscale(1) sepia(.4) hue-rotate(50deg) saturate(2.2) brightness(.5) contrast(1.25) blur(1.5px)'
def face_xy(img):
    """Face centre in 1080x1350 post coordinates (background is cover-fitted and centred)."""
    im = cv2.imread(img); H, W = im.shape[:2]
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY); best = None
    for c in ['haarcascade_frontalface_default.xml', 'haarcascade_profileface.xml']:
        f = cv2.CascadeClassifier(os.path.join(os.path.dirname(os.path.abspath(__file__)), c)).detectMultiScale(g, 1.1, 5, minSize=(W // 25, W // 25))
        for (x, y, w, h) in f:
            if best is None or w * h > best[2] * best[3]: best = (x, y, w, h)
    s = max(1080 / W, 1350 / H); ox = (W * s - 1080) / 2; oy = (H * s - 1350) / 2
    if best is None: return None
    x, y, w, h = best
    return ((x + w / 2) * s - ox, (y + h / 2) * s - oy)
def layered(img, num, hl, meta, cr, tag, out, size=None):
    """img: AI player image. num: big stat (e.g. '64*'). The number's centre goes on the face."""
    size = size or (600 if len(num) <= 2 else 520 if len(num) == 3 else 440)
    fc = face_xy(img)
    cx, cy = fc if fc else (540, 520)
    cy = min(max(cy, 330), 640)  # keep the number clear of the logo row and the headline block
    w = len(num) * size * 0.62
    if len(num) % 2 == 0: cx -= w / (2 * len(num))  # put a digit, not the gap between digits, on the face
    cx = min(max(cx, w / 2 + 20), 1060 - w / 2)
    top = max(cy - size * 0.42, 150)
    ns = f'font-size:{size}px;left:{cx - w/2:.0f}px;top:{top:.0f}px;width:{w:.0f}px;text-align:center;opacity:.93'
    post(img, os.path.join(os.path.dirname(__file__), 'none.png'), num, hl, meta, cr, tag, out, 'width:2px', ns, bgf=DUO)
    return fc
