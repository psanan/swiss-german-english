TODO for guide
<ul>
<li> Go through carefully
  <ul>
    <li> (start) add the terms here to translations file [would be nice to silence all warnings from script]
    <li> Polish/condense writing
  </ul>
<li> Iterate until happy
  <ul>
    <li> Resolve all TODOs in text
    <li> Fix N (500? 444? 333? Less even?) and cut down (make each entry count!)
    <li> This doc should be max  2N lines
    <li> Make as short as possible! (prioritize the things furthest from High German, choose most powerful examples.)
      <li> Fiddle with appearance
<li> (finish) translations file
    <li> Convert/remove existing .txt files and remove them
    <li> Attempt to recheck all entries (maybe add columns to tsv for source?) [especially possessives, pronouns, etc. which will certainly have errors]
  </ul>
<li> Write scripts to generate flashcards (and quiz?) from tsv output from processing this file
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
<li> My own experience living in Zurich (unreliable) and information from my 4-year old (fluent, but also unreliable).
</ul>

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
* Full sentences (which should then end with punctuation)
* Words which are always capitalized

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
