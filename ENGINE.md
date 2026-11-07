# Elova Sports engine (renders Elova Sports News, the 3-a-day latest-news posts)

Renders the posts for the `main` branch (images/ + captions/), which Make.com posts at 14:00, 18:00, 22:00 PKT.

## Setup in a fresh session
git clone -b engine https://github.com/g-murtaza44/elova-sports-autopost engine && cd engine && ./setup.sh

## Render a batch
Write playbook3/<batch>.py defining N = {"YYYY-MM-DD-slot": html, ...} then `posts.clear(); posts.update(N)`.
Run: cd /home/claude/playbook3 && BATCH=<batch> FONTSET=archivo OUT=<dir> python3 make.py
Layouts (see people.py / make.py):
- RETIRED (old logo, never use): comp(), full(), panel(), bigstat(), cover(), listcard(), rulecard(). Use v2/v2.py post() only.
- comp(bg_photo, sport, date, num, headline, cutout_png, credit, h, right, top, numsize) : real player cutout on a scene photo, big lime number. Preferred for any post about a person.
- full(photo_in_commons, object_position, sport, date, num_or_None, headline, credit) : real match photo full bleed.
- panel(photo_in_commons, sport, date, headline, credit, ph, pos, num) : landscape real photo on top, text below.
- bigstat(img(P+'scene.jpg',...), sport, date, num, headline) / cover(...) : scene only, when no free photo of the person exists.
Headline: put 1 to 2 key phrases in <b>..</b> (lime highlight). Keep the <b> phrase short so it fits one line.
Scene photos: photos/ (adelaide, cfield, delhi = cricket grounds; pitch, goal = football; track; pool; squash; tennis_a/b; baseball_a/b).

## Real player photos (free licences only)
Wikimedia Commons blocks direct downloads from the session, so photos are fetched by GitHub Actions on branch `assets`:
edit tools/queries.txt (one search per line, e.g. "Harry Kane Bayern"), push to `assets`, wait ~2 min, pull; results in found/ (index.json has licence, author, date).
Cut out with: python3 /home/claude/scripts/cut.py <name>  (expects /home/claude/commons/<name>.jpg, writes <name>_cut.png).
Every photo needs a credit line: author + licence. Never use agency/news photos or AI images of real people.

## Rules
- FACES FIRST (GM's request): every Elova Sports News post should show the real person the story is about whenever a free-licence photo exists. Search Commons with 2 to 3 different queries (name + club, name + national team, name + sport) before falling back to a scene-only layout. A team story uses its captain, scorer or star player.
- FLAGS (GM's request): when a story involves national teams or a player's country, add flags with flag(cc) or vs(cc1, 'TEAM1', cc2, 'TEAM2') from people.py (flag-icons, MIT; codes: pk, in, lk, au, gb-eng, za, nz, us, br, ar, fr, es ...). Typical place: the date line, e.g. date=vs('pk','PAKISTAN','lk','SRI LANKA'). For club stories, use the player's country flag only if it adds meaning. Never use club or league logos.
- GM's favourite look: part of the player (bat, racket, glove, arm, ball, helmet) sits IN FRONT of the big lime number, like the Lara 400* post (cutout layer is above the number). Do this on every comp() post where it looks natural: place the cutout so an object or limb overlaps roughly a quarter of the number. Never hide the face, never make the number unreadable, never force a strange crop. Check the render.
- Weekly batch = recent finished events (last 7 days) and hooks for events happening that day. History is parked in main/parked/.
- No em dashes. Plain direct English. Sport + competition in the top-right tag, date line above the headline, opponent named.
- Caption: hook line, 1 to 2 factual sentences with date and venue, optional question, 3 to 4 hashtags ending #ElovaSports.

## FIXED ELEMENTS: NEVER CHANGE (GM, 1 Nov 2026, applies to Elova Sports AND Nuvrio)
- Headline: Archivo Black, ALL CAPS, centred, 58px, white; key phrase in a solid LIME BOX (#C8F031) with dark green text (#07160E). Reference: main/images/2026-10-31-3.png (Mbangula). Built into v2/v2.py, mark the phrase with <em>..</em>.
- Bottom row: 4 white circle social icons, black logos: Facebook, Instagram, X, LinkedIn, centred at the bottom. Built into v2/v2.py (ICONS).
- "Image is AI generated and is just for reference" goes ONLY at the end of the CAPTION. NEVER on the image. Pass credit '' for AI images.
- Nuvrio: same idea with its own approved template; never change its headline highlight, fonts/sizes or social icons.

## KITS (AI back-view images must match)
- Pakistan ODI/T20I: green shirt, light green at the top fading to dark green at the bottom, subtle star pattern on the chest, dark green trousers, dark green helmet. Name and number on the back in WHITE, bold block capitals. Pink kit only on announced breast-cancer days (e.g. 18 and 25 Oct 2026).
- Shirt numbers: verified only (Arafat Minhas 90 per Wikipedia; Fakhar Zaman 39). If a number cannot be verified, put the surname only.
- Other teams: research the current kit colours before prompting, then add a line here.
- Marseille football: white shirt, light sky-blue collar and cuffs (v2/kits/marseille_football.jpg); name on the back in dark navy, Graduate. Gouiri number unverified, surname only.
- NOTE: assets tools/cf_prompts.txt and cut_list.txt are processed in FULL on every push; keep only the new lines in them.
- West Indies Test: plain white shirt and trousers (v2/kits/westindies_test_cricket.jpg); name on the back in maroon (#6E1A2B), font Graduate. Amir Jangoo number unverified, surname only.



## NO PLAYER PHOTO: LOCKED WAY (GM approved 3 Nov 2026, "lock, use such way in such cases")
1. Real free photo of the player in the story's kit: use it (cutout).
2. AI PLAYER IMAGES ARE OFF (GM, 7 Nov 2026: the Jangoo 111* AI back-view looked fake: pasted cutout, wrong lighting, flat name, no number). Do NOT use Cloudflare/any AI player image until GM approves a new sample. Skip straight to step 3 (flags) or 4 (stadium).
   (old, disabled) Cloudflare AI (1 Lucid Origin image per day, resets 05:00 PKT): spend it on the day's biggest post without a photo, as a back-view player in the right kit (name and number added in HTML). Save every AI image as a reusable kit in engine v2/kits/<team>_<sport>.jpg and reuse kits on later days before spending the daily quota again. Never waste the quota on retries or tests.
3. Every other post without a usable photo where countries are involved: FLAG DESIGN. from flagbg import flag_bg; one country = flag_bg('et'); two national teams = flag_bg('nz','in') (first = left team, second = right team; split diagonally with a lime line). Pass it as the post() background with no cutout ('width:2px'), bgf='brightness(.58) saturate(1.05)', big number centred-left. Flag codes from flag-icons (pk, in, gb-eng, nz, au, za, lk, bd, us, et, ke, de, ca, ...).
4. Club-only stories (no national team, e.g. Barcelona v Alaves): no flags and no club crests; use the sport's stadium background from v2/bg/.
Never post an empty background when one of these is possible.

## HARD RULES (GM, 3 Nov 2026) - check EVERY post before pushing, News and Records alike
1. LOGO: only the v2 logo (dark square with white E and lime bar, plus "ELOVA / SPORTS" text) exactly as v2/v2.py draws it. Never use the old playbook3 layouts (bigstat, listcard, rulecard, comp, full, panel, cover) because they carry the old logo. Every post, including lists and rules cards, is made with v2/v2.py.
2. SOCIAL ICONS: the 4 white icons (Facebook, Instagram, X, LinkedIn) at the bottom of EVERY post. post() adds them; never remove or hide them.
3. BACKGROUND MATCHES THE SPORT. Never put a non-cricket story on a cricket ground. v2/stadium_crowd.jpg is CRICKET ONLY. Use v2/bg/<sport>.jpg: athletics (running track), swimming (pool), football (football stadium/pitch), cricket, f1 (race circuit), tennis (court), basketball (arena court), baseball, weightlifting (gym/platform), cycling (velodrome/road), golf, rugby, boxing/mma. If the file for a sport is missing, get a dramatic free Unsplash photo of that sport's venue (night/lights preferred), save it as v2/bg/<sport>.jpg in the engine branch and commit it so it is reused.
4. KIT MATCHES THE STORY: a player photo must show the kit of the team in the story (club story = club shirt, national story = national shirt). Wrong shirt = do not use it; use the AI back-view in the right kit or scene-only.
5. Before pushing, look at each final PNG and confirm 1, 2, 3 and 4. If any fails, fix it before pushing.

## STYLE V2 (DEFAULT from 31 Oct 2026, GM loves it)
- Use v2/v2.py post(bg, cutout, num, headline, meta, credit, tag, out, cutstyle, numstyle, bgf) for every News post. Older comp()/bigstat() layouts are retired.
- Look: full-bleed dramatic photo of THE STORY'S SPORT venue from v2/bg/<sport>.jpg (see HARD RULES; stadium_crowd.jpg = cricket only), big lime number, real player cutout in front of the number (bat/arm overlapping, Lara 400* idea), Title Case headline with key words in <em> (lime), flags via meta line, big logo top-left, sport pill top-right.
- Cutouts: do NOT use local rembg u2net (soft, odd edges). Add "name.jpg URL" lines to tools/cut_list.txt on the assets branch and push; workflow cut.yml runs BiRefNet (portrait + general) on GitHub and commits cut/<name>_birefnet-*.png. Pull, erase other people/objects with PIL if needed, check on a dark background.
- Prefer action/celebration photos over posed ones; always check the original full photo, the best moment (raised bat etc.) may be outside the old crop.
- No AI images of real, named athletes.
- NO GOOD PLAYER PHOTO? See 'NO PLAYER PHOTO: LOCKED WAY' (AI players OFF since 7 Nov). Never post an odd/blurry cutout. Fallback order: (1) real Unsplash photo of an anonymous player seen from behind / celebrating; (2) GM's AI back-view: AI image from Cloudflare Workers AI (free): put 'key|prompt' in assets tools/cf_prompts.txt and push; cf.yml runs Leonardo Lucid Origin at 1080x1350 and commits ai/key_lucid-origin.jpg (also a flux-1-schnell version). FREE LIMIT: 10,000 neurons/day (resets 00:00 UTC = 05:00 PKT); one Lucid Origin image uses most of it, so ONE AI image per day, one push, no retries. Use lucid-origin. Do NOT use Pollinations (ai.yml): blurry, garbled text. Gemini API images are not free (429) of a player seen from BEHIND, celebrating, wearing a plain jersey in the team's real kit colours for that series, with NO face, NO text, NO logos in the prompt. Then add the real player's SURNAME and SHIRT NUMBER on the back of the jersey yourself in HTML/CSS (font 'Jersey 10' or 'Graduate' from fonts/node_modules/@fontsource, colour matching that series' kit, slight perspective/opacity so it sits on the fabric). Verify the shirt number for that series. No team crests, sponsor logos or copied official kit fonts. Put "Image is AI generated and is just for reference" at the end of the caption only, never on the image. Never an AI face.
- TOKEN BUDGET: GM's Claude credits are limited. Be efficient: no re-renders unless something is actually broken, look at each final PNG once, keep research to what the posts need, no long reports.

## ELOVA SPORTS RECORDS (2 posts/day, weekly batch)
- Files: main/records/YYYY-MM-DD-1.png/.txt (12:00 PKT) and -2 (20:00 PKT).
- Content: world records recently broken (most recent first: last weeks/months; athletics, swimming, cricket, football, F1, weightlifting, esports-free). Verify each record in a reliable source. Big number = the record (time, score, count).
- Same STYLE V2 template, tag pill e.g. "WORLD RECORD · ATHLETICS". Same photo and AI fallback rules.

- Number must stay readable: the cutout may overlap only the edge of the number, never hide a digit. If a cutout has hard crop edges or other people that cannot be removed cleanly, use the scene-only layout (cutout 'none').
