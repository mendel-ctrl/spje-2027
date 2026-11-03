"""
Build the Ticket Tailor version of the event description.

Usage:
    python3 build.py

Reads  event-description.html  (photos linked as photos/xxx.jpg)
Writes dist/ticket-tailor.html  (photos linked to the public GitHub Pages site,
                                 ready to paste into Ticket Tailor's </> code view)

Set PHOTO_BASE_URL below to your GitHub Pages address once Pages is turned on.
"""
import os
import re

# Example: "https://mendel-ctrl.github.io/spje-2027/"
PHOTO_BASE_URL = "https://mendel-ctrl.github.io/spje-2027/"

PLACEHOLDER = "https://placehold.co/600x600/120d24/a48bff?text={}"

src = open("event-description.html", encoding="utf-8").read()


def swap(match):
    path = match.group(1)
    if os.path.exists(path):
        return 'src="' + PHOTO_BASE_URL.rstrip("/") + "/" + path + '"'
    # Photo not added yet: show a labelled purple placeholder instead of a broken image
    name = os.path.splitext(os.path.basename(path))[0]
    print(f"  missing photo: {path} (using placeholder)")
    return 'src="' + PLACEHOLDER.format(name) + '"'


out = re.sub(r'src="(photos/[^"]+)"', swap, src)
os.makedirs("dist", exist_ok=True)
open("dist/ticket-tailor.html", "w", encoding="utf-8").write(out)
print("Wrote dist/ticket-tailor.html")
