TODO for guide
<ul>
<li> Iterate until happy
  <ul>
    <li> Resolve all TODOs in text
    <li> Fix N (500? 444? 333? Less even?) and cut down (make each entry count!)
    <li> The guide should be max 2N lines
    <li> Make as short as possible! (prioritize the things furthest from High German, choose most powerful examples.)
    <li> Simplify translation by chooisng conventions (see below) and removing distracting duplicates (e.g. "e" vs "ä" variants, etc.)
    <li> Fiddle with appearance
    <ul>
    <li> Tables?
    </ul>
    <li> Attempt to recheck all entries (maybe add columns to tsv for source?) [especially possessives, pronouns, etc. which will certainly have errors]  (maybe try and get Swissing teacher to look, if I have a solo lesson..)
  </ul>
<li> A way to get flashcards. Either wwrite scripts to generate flashcards from tsv output from processing this file, or get it work with a data dump and something FOSS like Anki.
<li> Move the whole thing to psanan.github.io repo?
<li> Publish and get feedback!
<li> Think about chopping audio from the Swissing material and/or Luana mulirama podcasts! (wont' be complete, but audio clips are essential here..) (would be useful to go through that, anyhow)
</ul>

# Swiss German to English

Resources for a native English speaker, with knowledge of High German,
to learn Swiss German.

1. A reference for valid Zurich Swiss German to High German and English translations

2. A guide presenting a small subset of these to bring understanding of Swiss German closer to understanding of High German

## Sources

<ul>
<li> A1 Swiss German lectures and course materials from <a href="https://swissing.ch/">Swissing</a>
<li> <a href="https://www.sergiojlievano.com/hoi">Hoi! Your Swiss German Survival Guide</a>
<li> <a href="https://eldrid.ch/switzerland.htm">Eldrid's Swiss German pages</a>
</ul>

## Guides

This repository includes the data and logic to generate guides for learning, reference, and practice.

* TODO: link to Guide. Word list. and/or Flashcards.

## Scope and data conventions

The main data source is [translations.tsv](./translations.tsv), a small set of
translations of Swiss German strings to English and optionally High German
ones.

We present a curated set of examples to cover as much of the difference between
High German and Zürich Swiss German as possible.

It's not a complete reference or dictionary.
It's not gentle - it expects you
to think critically about the examples, which may demonstrate more than one
concept.  The aim is, however, that it's 100% accurate, to the extent that the language is even well-defined.
I am 100% sure I have not attained
this goal. If you (especially if you're a native Zürich Swiss German speaker)
find a mistake, please open an issue or pull request for this repository.

Interesting usage and differences from High German should be shown, not told.
Clarify by using longer examples, e.g.  since "mir" can mean both "we" and "to
me", include entries like "mir sind" and "mit mir".

A given Swiss German string should only appear in a single entry. Entries can
have multiple strings in each language. Not tabs are allowed. Any of the English or High German
strings must be a valid translation of any of the Swiss German strings.  This
covers variations both in spelling (which should only be relevant for Swiss German),
interchangeable strings in the source language (e.g. "doch" and "moll" in Swiss
German), and multiple valid translations in the target languages.

Strings should not be capitalized, except for
* Full sentences (which should then end with punctuation)
* Words which are always capitalized

Parenthesized expressions should generally be avoided in the examples,
preferring examples which don't require them, or multiple valid translations.
If included, entries should be valid, up to whitespace, as if individual
strings with and without the parenthetical expressions were included.

This guide is not self-consistent with respect to Swiss German orthography.
In general, when choosing between equally-valid spelling options, prefer:

- shorter forms over longer ones
- "aa" over "ah" (gaats)
- "e" over "ä" (wie)
- "o" over "oo" (cho)
- "oi" over "eu" (ois)
- "d" over "t" (Dütsch)
- "b" over "p" (Bire)
