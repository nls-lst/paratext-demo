# paratext workshop

A worked example of [paratext](https://github.com/nls-lst/paratext): turning a
box of scanned catalogue cards into structured metadata with a multimodal model,
then reviewing what the model got wrong.

Everything here is public domain — 50 Boston Public Library rare-books catalogue
cards. See [`data/README.md`](data/README.md).

## Getting set up

**In a Codespace** (recommended): press `.` or use the green **Code** button →
**Codespaces** → **Create codespace**. Everything installs itself; when the
terminal settles you're ready.

**On your own machine**, you need [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/nls-lst/paratext-demo
cd paratext-demo
uv sync
```

You need an API key in `PARATEXT_API_KEY`. In a Codespace it is already there.

## 1. Look before you run

```bash
uv run paratext inspect -p bpl-cards
```

This prints the fields the model is asked for, the prompt it will be sent, and
whether schema, prompt and view still agree. It describes what is **installed**,
so if it disagrees with the files you're editing, the package needs reinstalling.

## 2. Run it

```bash
uv run paratext run -p bpl-cards --limit 5
```

Five cards, five model calls, about a minute. It writes
`output/bpl-cards.jsonl` and packages a review round in `review/`.

## 3. Look at what it did

```bash
uv run paratext review
```

Opens the review UI on port 5050 — in a Codespace, VS Code offers to open it.
Go through the five cards against the images. Some will be right. Look for:

- **Continuation cards.** Some cards end "(Continued on next card)". What did
  the model put in `notes`? What *should* a record do here?
- **Markup.** Watch for HTML creeping into the title of anything with a
  superscript.
- **Empty fields.** Did it leave `heading` null, or invent one?

## 4. Fix the prompt

This is the actual work. `bpl_cards/prompt.md` is deliberately thin — it names
each field and stops. Add the rules you just found yourself wanting, then:

```bash
uv run paratext run -p bpl-cards --limit 5 --re-extract
```

`--re-extract` matters: a run resumes on sample id, so without it your five
cards are already in the output file and the model is never called. (paratext
will stop and tell you this rather than pretending to work.)

Because the prompt changed, this is **round 2**. The review UI shows r1 and r2
side by side and highlights what moved. That loop — run, review, edit the
prompt, run again — is the whole method.

## 5. Export

```bash
uv run paratext export -p bpl-cards --format marc
```

Approved records out as MARCXML (or `--format dc`, or `hf` for a Hugging Face
dataset).

## Where to go next

- `bpl_cards/schema.py` — add a field, and see `inspect` complain until the
  prompt mentions it too.
- The [paratext README](https://github.com/nls-lst/paratext) — `paratext new`
  scaffolds this same structure for your own collection.
