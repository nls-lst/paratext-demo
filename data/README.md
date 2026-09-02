# The cards

50 catalogue cards from the Boston Public Library's Rare Books Department,
sampled from [`biglam/bpl-card-catalog`](https://huggingface.co/datasets/biglam/bpl-card-catalog)
(~838,000 cards digitised via the Internet Archive).

**Licence: CC0 1.0** — public domain dedication. They can be redistributed,
modified and used commercially with no conditions.

`cards-meta.json` carries, for each image, the drawer and card number, the
`source_url` of the Internet Archive item it came from, and `ocr_text` — the
OCR the dataset ships with.

That OCR is worth looking at before you run anything. For the card that reads
"The Elizabethan stage", it begins:

    )\nPN2589 C4 Chambers, Sir Edmund Kerchever, 1866- The Elizabethan stage.

Everything is there and nothing is structured: no way to tell the call number
from the author, the heading from the title. That gap — between text on a page
and metadata you can catalogue with — is what paratext exists to close.
