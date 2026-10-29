# Elova Sports autopost

Make.com posts the files whose name matches today's date (Pakistan time). One post a day at 9 PM.

| Folder | What | Named |
|---|---|---|
| images/ | The post image (Instagram, Facebook, LinkedIn) | YYYY-MM-DD.png |
| captions/ | The caption | YYYY-MM-DD.txt |

Raw file links for Make:
- https://raw.githubusercontent.com/g-murtaza44/elova-sports-autopost/main/images/{{formatDate(now; "YYYY-MM-DD"; "Asia/Karachi")}}.png
- https://raw.githubusercontent.com/g-murtaza44/elova-sports-autopost/main/captions/{{formatDate(now; "YYYY-MM-DD"; "Asia/Karachi")}}.txt

If a file is missing for a date, that day is skipped.
