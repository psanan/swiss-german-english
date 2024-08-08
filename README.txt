# Swiss German to English

Resources for a native English speaker, with some knowledge of High German,
to learn Swiss German.

1. A reference for valid Zurich Swiss German to English translations

2. A guide presenting a small subset of these to bring understanding of Swiss German closer to understanding of High German

TODO organization (jot files, main JSON, guide)

## Scope and data

This is not a complete reference or dictionary (see sources for examples of those).

Rather, it is a curated set of examples to help someone (roughly like me) learn. 

Thus, data directly stored can be minimal, fundamentally
just a set of pairs of strings, one in Swiss German and one in English.

In any translingual dictionary, there will be multiple translations of a given
term in one language. Further, the mapping between languages is not invertible,
as words have multiple, context-dependent meanings. There are two separate but related
issues here, as Swiss German isn't standardized:

1. Even within Zurich Swiss German, there are significant differences in how people speak
2. For identical speech, there are multiple written forms

To address these:

Data here prioritizes the Swiss German to English mapping. That is, without other context,
what's the most likely English translation of the Swiss German string? 

For multiple, different-sounding, valid Zurich Swiss German ways to say the same thing, raw data includes
multiple entries.

For variations purely to do with spelling, entries can have any number of alternate Swiss German
strings. 
TODO: decide if we actually even need this. With a convention on e.g. e/ä and parentheses, we might not need it.
TODO: decide if we will have a primary chde representation, or just multiple options.
TODO: decide if we will natively support parentheses e.g. "cha(n)" or "cho(o)".
TODO: decide if we will adopt the Swissing textbook conventions as preferred or not.



