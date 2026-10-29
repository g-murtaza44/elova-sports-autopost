# Elova Sports engine

Renders the posts for the `main` branch (images/ + captions/), which Make.com posts at 14:00, 18:00, 22:00 PKT.

## Setup in a fresh session
git clone -b engine https://github.com/g-murtaza44/elova-sports-autopost engine && cd engine && ./setup.sh

## Render a batch
Write playbook3/<batch>.py defining N = {"YYYY-MM-DD-slot": html, ...} then `posts.clear(); posts.update(N)`.
Run: cd /home/claude/playbook3 && BATCH=<batch> FONTSET=archivo OUT=<dir> python3 make.py
Layouts (see people.py / make.py):
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
- Weekly batch = recent finished events (last 7 days) and hooks for events happening that day. History is parked in main/parked/.
- No em dashes. Plain direct English. Sport + competition in the top-right tag, date line above the headline, opponent named.
- Caption: hook line, 1 to 2 factual sentences with date and venue, optional question, 3 to 4 hashtags ending #ElovaSports.
