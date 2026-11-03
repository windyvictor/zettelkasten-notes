# zettelkasten-notes

English | [中文](README.cn.md) · [Research Skillbox](https://github.com/windyvictor/research-skillbox)

A Zettelkasten skill for turning reading, lectures, conversations, and research into reusable notes, connecting them with evidence, and using them to support writing and thinking.

## Why this skill

A note archive can grow for years without producing a single argument. Zettelkasten works when notes are understandable on their own, faithful to their sources, linked for a stated reason, and repeatedly reused in new thinking and writing. This skill treats the vault as a production system rather than a storage collection.

### What you get

- Source-faithful fleeting, literature, permanent, or project-note drafts
- Connections that state whether one card supports, contradicts, extends, or applies another
- Human-review states for AI-generated candidates
- Paragraphs, outlines, or article structures grown from existing cards
- Read-only vault audits for broken links, duplicate titles, stale drafts, and review problems

**Workflow:** capture the source → restate one usable idea → find and explain real connections → keep uncertain material in draft → reuse notes in an output.

## Use it for

- Drafting fleeting, literature, permanent, or project notes
- Reviewing whether a card is self-contained and source-faithful
- Connecting cards and handling conflicts with older claims
- Growing a paragraph, article, or paper from existing cards
- Auditing a vault for broken links, duplicates, and draft states
- Managing AI-generated note candidates with human-review gates

Deep reading of a paper belongs to a paper-reading workflow; use this skill when the result needs to become a note.

## Contents

- `SKILL.md`: task routing, write boundaries, and completion rules
- `references/`: note writing, linking, reuse, and AI collaboration
- `assets/`: card, vault-rule, launch-plan, and review-log templates
- `scripts/check_card.py`: single-card review hints
- `scripts/lint_vault.py`: read-only vault audit
- `evals/`: trigger, task, and vault fixtures
- `tests/`: checker regression tests

## Core rule

A note must first remain faithful to its source. AI output stays in draft state until a person checks the claim, source, conditions, and links. An unlinked draft is valid when no real connection exists.

## Quick checks

```bash
python3 scripts/check_card.py card.md
python3 scripts/lint_vault.py /path/to/vault
python3 -m unittest discover -s tests -v
```

The scripts provide mechanical hints. Attribution, context, length, and semantic link quality still require judgment.

## Install

```bash
git clone https://github.com/windyvictor/zettelkasten-notes.git
ln -s "$PWD/zettelkasten-notes" ~/.agents/skills/zettelkasten-notes
```

## License

MIT. Third-party ideas, quotations, and source materials retain their original rights.

