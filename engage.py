"""Elova engagement bot (TEST). Separate from the posting engine.
Likes fresh posts and leaves short English comments on a few cricket pages.
Safe defaults: DRY_RUN=1 (does nothing but print). Low caps, human delays,
stops at the first Instagram warning. Needs secret IG_SESSIONID (+ optional IG_CSRF, IG_DS_USER_ID)
from the TEST account's own browser. Comments are written by Cloudflare Workers AI (free).
"""
import os, sys, json, random, time, re, urllib.request
from playwright.sync_api import sync_playwright

DRY = os.environ.get("DRY_RUN", "1") != "0"
MAX_LIKES = int(os.environ.get("MAX_LIKES", "6"))
MAX_COMMENTS = int(os.environ.get("MAX_COMMENTS", "2"))
PAGES = os.environ.get("PAGES", "therealpcb,icc,cricinfo,homeofcricket,localleggie").split(",")
CF_ACCOUNT = os.environ.get("CF_ACCOUNT_ID", "")
CF_TOKEN = os.environ.get("CF_API_TOKEN", "")
BAD = re.compile(r"(try again later|action blocked|suspicious|confirm it'?s you|checkpoint|challenge)", re.I)
RISKY = re.compile(r"(politic|modi|india|israel|gaza|religio|islam|hindu|bet|gambl|fix|scam|hate|kill|dead|died|injur)", re.I)

def log(*a): print("[engage]", *a, flush=True)
def pause(a=6, b=14): time.sleep(random.uniform(a, b))

def write_comment(caption):
    """Short, smooth English, ends with a question. Returns None if unsafe."""
    if not (CF_ACCOUNT and CF_TOKEN) or RISKY.search(caption or ""):
        return None
    prompt = ("Write ONE Instagram comment (max 2 short lines, max 2 emojis, no hashtags, no links, "
              "warm natural English, not robotic) for a cricket post with this caption. "
              "Be factual, positive, no politics, no India-Pakistan rivalry, no betting. "
              "End with a simple question that invites replies. Output only the comment.\n\nCaption: " + caption[:500])
    req = urllib.request.Request(
        f"https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT}/ai/run/@cf/meta/llama-3.1-8b-instruct",
        data=json.dumps({"messages": [{"role": "user", "content": prompt}]}).encode(),
        headers={"Authorization": f"Bearer {CF_TOKEN}", "Content-Type": "application/json"})
    try:
        txt = json.load(urllib.request.urlopen(req, timeout=60))["result"]["response"].strip().strip('"')
    except Exception as e:
        log("comment gen failed", e); return None
    if len(txt) > 220 or RISKY.search(txt) or "#" in txt or "http" in txt:
        return None
    return txt

def main():
    sid = os.environ.get("IG_SESSIONID", "")
    if not sid and not DRY:
        sys.exit("IG_SESSIONID missing")
    likes = comments = 0
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        ctx = b.new_context(viewport={"width": 1280, "height": 900}, locale="en-US",
                            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36")
        if sid:
            ck = [{"name": "sessionid", "value": sid, "domain": ".instagram.com", "path": "/", "secure": True, "httpOnly": True}]
            for n, e in (("csrftoken", "IG_CSRF"), ("ds_user_id", "IG_DS_USER_ID")):
                if os.environ.get(e): ck.append({"name": n, "value": os.environ[e], "domain": ".instagram.com", "path": "/", "secure": True})
            ctx.add_cookies(ck)
        pg = ctx.new_page()
        pg.goto("https://www.instagram.com/", wait_until="domcontentloaded"); pause(4, 8)
        if BAD.search(pg.content()[:20000]) or "/accounts/login" in pg.url:
            log("STOP: not logged in or Instagram challenge. Nothing done."); return 2
        random.shuffle(PAGES)
        for page in PAGES:
            if likes >= MAX_LIKES: break
            pg.goto(f"https://www.instagram.com/{page.strip()}/", wait_until="domcontentloaded"); pause(5, 10)
            if BAD.search(pg.content()[:20000]): log("STOP: warning shown"); return 3
            links = pg.eval_on_selector_all("a[href*='/p/'], a[href*='/reel/']", "e=>e.slice(0,3).map(x=>x.href)")
            for url in links[:2]:
                if likes >= MAX_LIKES: break
                pg.goto(url, wait_until="domcontentloaded"); pause(5, 10)
                if BAD.search(pg.content()[:20000]): log("STOP: warning shown"); return 3
                cap = (pg.locator("h1").first.inner_text() if pg.locator("h1").count() else "")[:600]
                like = pg.locator("svg[aria-label='Like']").first
                if like.count():
                    log(("DRY would like " if DRY else "like ") + url)
                    if not DRY: like.click(); pause(4, 9)
                    likes += 1
                if comments < MAX_COMMENTS:
                    c = write_comment(cap)
                    if c:
                        log(("DRY would comment " if DRY else "comment ") + url + " -> " + c)
                        if not DRY:
                            box = pg.locator("textarea[aria-label^='Add a comment']").first
                            box.click(); box.type(c, delay=random.randint(60, 140)); pause(2, 4)
                            pg.get_by_role("button", name="Post").first.click(); pause(8, 15)
                        comments += 1
        b.close()
    log(f"done likes={likes} comments={comments} dry={DRY}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
