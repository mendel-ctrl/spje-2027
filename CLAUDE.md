# St. Pete Jewish Experience 2.0 — Ticket Tailor event page

Owner: Mendel Lebovics, Chabad of St. Petersburg (GitHub: mendel-ctrl).
Mendel is a beginner at coding: explain every step plainly, one step at a time.

## What this is
The event description for "The St. Pete Jewish Experience 2.0" on Ticket Tailor.
Sunday, January 10, 2027, 5:00 PM, The Floridian Social, downtown St. Petersburg.
Lineup: 8th Day (headliner), the Lebovics Brothers Choir, comedian Eli Lebowicz (spelled Lebowicz, NOT Lebowitz).

## Files
- `event-description.html` — the source. Edit this one. Photos are linked as `photos/name.jpg`.
- `photos/` — all photos, already cropped and sized. `lebovics-brothers.jpg` is still missing.
- `build.py` — run `python3 build.py` to make `dist/ticket-tailor.html`, where photo links point to
  the public GitHub Pages site. That file is what gets pasted into Ticket Tailor.
- `index.html` — preview page for GitHub Pages (open it in a browser to see the design).
- `reference/` — the event poster and the website-style inspiration image.

## Rules for Ticket Tailor (learned the hard way)
- Paste into the Description editor's code view (`</>` button).
- ALL styling must be inline `style="..."`. No `<style>` tags, no `<script>`, no external CSS.
- Ticket Tailor DELETES photos embedded as `data:` (base64) URIs. Photos must be real https links
  (GitHub Pages works) or uploaded through Ticket Tailor's own Replace button.
- Ticket Tailor keeps inline styles, colors, fonts, inline-block layouts, and the YouTube iframe
  wrapped in `<div class="embed-content embed-responsive">`.
- Keep the whole thing inside one outer `<div>`, max-width 900px.

## Design
Dark concert-website style (inspired by reference/style-inspiration.jpg), colors from the poster:
background #0a0910, accent purple #a48bff, button purple #5b3fe0, white headings.
Script accents use 'Brush Script MT', 'Segoe Script', cursive.
Four "Buy Tickets" buttons link to https://www.tickettailor.com/events/chabadjewishcenterofstpetersburg/2511961
(confirm this link works once the event is published).
Sponsorship tiers: Diamond $18,000, Platinum $10,000, Gold $7,200, Silver $5,000, Am Yisrael Chai $1,800.
Sponsor/questions email: info@chabadsp.com.

## Workflow
1. Edit `event-description.html` (or add photos to `photos/`).
2. Run `python3 build.py`.
3. Commit and push to GitHub (photos go live on GitHub Pages within a minute or two).
4. Copy `dist/ticket-tailor.html` into Ticket Tailor's code view and save.
