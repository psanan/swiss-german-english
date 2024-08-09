# Swiss German to English

Resources for a native English speaker, with some knowledge of High German,
to learn Swiss German.

1. A reference for valid Zurich Swiss German to English translations

2. A guide presenting a small subset of these to bring understanding of Swiss German closer to understanding of High German

## Scope and data

This is not a complete reference or dictionary (see sources for examples of those).

Rather, it is a curated set of examples to help someone (roughly like me) learn.

Thus, data directly stored can be minimal, based on giving a small set of useful, correct translations
of Swiss German strings to English ones.

In any translingual dictionary, there will be multiple translations of a given
term. Further, the mapping between languages is not invertible,
as words have multiple, context-dependent meanings. For a non-standardized language
like Swiss German, there will also be many variations in usage, and further
in spelling.

To address non-invertibility, data prioritizes the Swiss German to English mapping:
Without other context, what is the most likely English translation of the Swiss German string?

To make it easier to detect duplicates, data entries can have multiple strings
in either language.
Any of the English strings must be a valid translation of any of the Swiss German strings.

We adopt the convention that anything in parentheses (plus a space if needbe)
can be removed and not affect validity of the translation. This is helpful
both to cover small variations in Swiss German spelling, e.g. "cho(o)", or for optional words
in English translations e.g. "to run (on foot)".

Data entries may optionally also include

* High German strings alongside English strings.
* Free-form comments in English

We store data as JSON, simply because this is a sufficient, human-readable format
natively supported by Python. In addition to helper scripts to read and write
this format, we also include a reader for "jot" files with a colon-separated Swiss German
and English strings on each line.
