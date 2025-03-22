#!/usr/bin/env python3
"""Define the data format and utilities to read to and from files.

The main data structure is an "entry", simply a
dict with keys KEYS and lists of strings as values."""

import csv

KEYS = ['ch', 'de', 'en']
PRIMARY_KEY = KEYS[0]
MAX_ALTERNATES = 3

# Each entry must have MAX_ALTERNATES entries:
TSV_COLUMN_KEYS = {
    'ch': ['CH 1', 'CH 2', 'CH 3'],
    'de': ['DE 1', 'DE 2', 'DE 3'],
    'en': ['EN 1', 'EN 2', 'EN 3'],
}


def entries_from_tsv(path):
    """Load entries from a TSV file.

    The file is expected to have columns with strings for each language
    as in TSV_COLUMN_KEYS.
    """
    rows = []
    entries = []

    with open(path, 'r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            rows.append(row)

    for row in rows:
        try:
            entry = {}
            for key in KEYS:
                entry[key] = []
                for column_key in TSV_COLUMN_KEYS[key]:
                    if row[column_key]:
                        # Strip for convenience
                        entry[key].append(row[column_key].strip())
        except:
            print(f"Error processing row: {row}")
            raise
        entries.append(entry)
    return entries


def _empty_row_dict():
    row_dict = {}
    for key in TSV_COLUMN_KEYS:
        for column_key in TSV_COLUMN_KEYS[key]:
            row_dict[column_key] = ""
    return row_dict


def _row_dict_to_string(row_dict):
    sub_strings = []
    for key in TSV_COLUMN_KEYS:
        for column_key in TSV_COLUMN_KEYS[key]:
            sub_strings.append(row_dict[column_key])
    sub_strings.append("\n")
    return "\t".join(sub_strings)


def _header_string():
    sub_strings = []
    for key in TSV_COLUMN_KEYS:
        for column_key in TSV_COLUMN_KEYS[key]:
            sub_strings.append(column_key)
    sub_strings.append("\n")
    return "\t".join(sub_strings)


def tsv_from_entries(entries, path):
    """Save a list of entries back to a TSV file."""
    with open(path, "w") as file:
        file.write(_header_string())
        for entry in entries:
            row_dict = _empty_row_dict()
            for key in KEYS:
                if key in entry:
                    tsv_alternate_index = 0
                    for alternate in entry[key]:
                        if tsv_alternate_index >= MAX_ALTERNATES:
                            raise Exception(
                                f"Only {MAX_ALTERNATES} alternates allowed but {entry} has more"
                            )
                        row_dict[TSV_COLUMN_KEYS[key]
                                 [tsv_alternate_index]] = alternate
                        tsv_alternate_index += 1
            file.write(_row_dict_to_string(row_dict))


def _validate_entry(entry):
    if entry is None:
        return False, "entry is None"
    if PRIMARY_KEY not in entry:
        return False, f"All entries require primary language key {PRIMARY_KEY}"
    return True, None


def validate_entries(entries):
    """Ensure that each entry is valid, and there are no duplicated values for the primary key."""
    primary_keys = set()
    for entry in entries:
        valid, status = _validate_entry(entry)
        if not valid:
            # It might be more convenient to print out all invalid entries first.
            return False, f"Invalid entry: {entry}: {status}"
        for entry_primary_keys in entry[PRIMARY_KEY]:
            if entry_primary_key in entry_primary_keys:
                return False, f"Duplicate primary key: {entry_primary_key}"
            primary_keys.add(entry_primary_keys)
    return True


def entries_by_primary_key(entries):
    """Requires validated entries list (no duplicates)"""
    entries_by_primary_key = {}
    for entry in entries:
        for entry_primary_key in entry[PRIMARY_KEY]:
            entries_by_primary_key[entry_primary_key] = entry
    return entries_by_primary_key


if __name__ == "__main__":
    test_entries = entries_from_tsv("translations.tsv")
    if not validate_entries(test_entries):
        print("Invalid!")
    else:
        print(entries_by_primary_key(test_entries))
        out_path = "translations_testout.tsv"
        print(f"Dumping to {out_path}")
        tsv_from_entries(test_entries, out_path)
