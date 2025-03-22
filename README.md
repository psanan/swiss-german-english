# Swiss German to English

Resources for a native English speaker, with knowledge of High German,
to learn Swiss German.

1. A reference for valid Zurich Swiss German to High German and English translations

2. A guide presenting a small subset of these to bring understanding of Swiss German closer to understanding of High German

## Guides

This repository includes the data and logic to generate guides for learning, reference, and practice.

* TODO: link to Guide. Word list. and/or Flashcards.

## Scope and data conventions

The main data source is [translations.tsv](./translations.tsv).

This is a curated set of examples to help someone (roughly like me) learn.
It's not a complete reference or dictionary.

Rather, it's aggressively example-based.  The underlying data is a small set of
translations of Swiss German strings to English and optionally High German
ones.

Interesting usage and differences from High German should be shown, not told.
Clarify by using longer examples, e.g.  since "mir" can mean both "we" and "to
me", include entries like "mir sind" and "mit mir".

A given Swiss German string should only appear in a single entry. Entries can
have multiple strings in each language.  Any of the English or High German
strings must be a valid translation of any of the Swiss German strings.  This
covers variations both in spelling (which should only be relevant for Swiss German),
interchangeable strings in the source language (e.g. "doch" and "moll" in Swiss
German), and multiple valid translations in the target languages.

Strings should not be capitalized, except for
* Full sentences
* Swiss German and High German nouns and other words (e.g. "Si") always capitalized.

Parenthesized expressions should generally be avoided in the examples, preferring
examples which don't require them, or multiple valid translations. If included,
they should only be in High German or English strings, and the translation should
be valid with or without the parenthesized expression (plus a space if needbe).

We try to be consistent with Swiss German orthography, but do aspire to perfection.
In general, we choosing between equally-valid spelling options, we prefer:

- shorter forms over longer ones
- "aa" over "ah"
- "e" over "ä"
- "o" over "oo"
- "oi" over "eu"
- "d" over "t"
- "b" over "p"
