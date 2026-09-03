# paratext demo

50 catalogue cards, a multimodal model, and an hour to find out how good the
output is. Cards are public domain — see [`data/README.md`](data/README.md).

**Start:** green **Code** button → **Codespaces** → **Create codespace on main**.
Wait for "Ready". Your API key is already set.

<details>
<summary>Running on your own machine instead</summary>

Needs [uv](https://docs.astral.sh/uv/) and an API key in `PARATEXT_API_KEY`:

```bash
git clone https://github.com/nls-lst/paratext-demo && cd paratext-demo && uv sync
```
</details>

---

## 1 · What is it about to do?

```bash
uv run paratext inspect -p bpl-cards
```

Seven fields, and the prompt that asks for them. Read the prompt — it is
`bpl_cards/prompt.md`, and it is the only thing you will change today.

## 2 · Run it

```bash
uv run paratext run -p bpl-cards --limit 5
```

Five cards, about a minute.

## 3 · Judge it

```bash
uv run paratext review
```

Open the forwarded port. Put a verdict on each of the five, against the image.

**This is the eval.** Not a benchmark score — five human judgements about
whether this output is usable. Note *what kind* of wrong each error is:

- Did it read the card wrongly, or read it right and file it wrongly?
- Is a field empty because the card is empty, or because the model gave up?
- Would you have to check every record, or only the ones it flagged?

## 4 · Fix the prompt

Open `bpl_cards/prompt.md`. Write the rule you found yourself wanting in step 3.
One rule at a time.

```bash
uv run paratext run -p bpl-cards --limit 5
```

The prompt changed, so this is **round 2**. Reload the review UI: r1 and r2 sit
side by side with the differences marked.

## 5 · Did it get better?

Judge round 2 the same way. Then ask the harder question: did your rule fix the
thing you aimed at, and did it break anything that was already right?

Repeat 4 and 5 while there is time. Five cards is small enough to iterate and
far too small to be sure — which is the last thing worth taking away.

---

<details>
<summary>Going further</summary>

- `--limit 20` for a wider run.
- `bpl_cards/schema.py` — add a field, and watch `inspect` complain until the
  prompt mentions it too.
- `uv run paratext export -p bpl-cards --format marc` — approved records out.
- [paratext](https://github.com/nls-lst/paratext) — `paratext new` scaffolds
  this same structure for your own collection.
</details>
