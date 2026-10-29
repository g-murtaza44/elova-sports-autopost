# Elova Sports autopost

Make.com posts 3 times a day (Pakistan time). Each run picks the files for today's date and the current slot.

| Slot | Time (PKT) | File ending |
|---|---|---|
| 1 | 2 PM | -1 |
| 2 | 6 PM | -2 |
| 3 | 10 PM | -3 |

| Folder | What | Named |
|---|---|---|
| images/ | The post image (Instagram, Facebook, LinkedIn) | YYYY-MM-DD-N.png |
| captions/ | The caption | YYYY-MM-DD-N.txt |

Raw file links for Make (one scenario, scheduled at 14:00, 18:00 and 22:00):
- https://raw.githubusercontent.com/g-murtaza44/elova-sports-autopost/main/images/{{formatDate(now; "YYYY-MM-DD"; "Asia/Karachi")}}-{{if(formatDate(now; "H"; "Asia/Karachi") = "14"; 1; if(formatDate(now; "H"; "Asia/Karachi") = "18"; 2; 3))}}.png
- https://raw.githubusercontent.com/g-murtaza44/elova-sports-autopost/main/captions/{{formatDate(now; "YYYY-MM-DD"; "Asia/Karachi")}}-{{if(formatDate(now; "H"; "Asia/Karachi") = "14"; 1; if(formatDate(now; "H"; "Asia/Karachi") = "18"; 2; 3))}}.txt

If a file is missing, that post is skipped.
