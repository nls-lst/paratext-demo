You are reading a catalogue card from the Boston Public Library's Rare Books
Department. Look at the image and return a single JSON object matching the
schema. Emit JSON only — no commentary or markdown.

- `call_number`: the shelfmark, usually printed down the left-hand edge.
- `heading`: the subject or added heading, usually typed in capitals across the
  top of the card. Leave it null when the card has none.
- `author`: the main entry — the personal or corporate name the card files
  under, transcribed as printed, including dates.
- `title`: the title of the work.
- `imprint`: place, publisher and date of publication.
- `collation`: the physical description — pagination, illustrations, size.
- `notes`: anything else the card records, such as a contents list.
