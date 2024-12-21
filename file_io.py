#!/usr/bin/env python3

import csv

PRIMARY_KEY = 'ch'
KEYS = ['ch', 'en', 'de']
TSV_COLUMN_KEYS = {
    'ch': ['CH 1', 'CH 2', 'CH 3'],
    'en': ['EN 1', 'EN 2', 'EN 3'],
    'de': ['DE 1', 'DE 2', 'DE 3']
}

# An entry is a dict with keys KEYS and lists of strings as values.


def validate_entry(entry):
    if entry is None:
        return False, "entry is None"
    if PRIMARY_KEY not in entry:
        return False, f"All entries require primary language key {PRIMARY_KEY}"
    return True, None


def validate_entries(entries):
    """Ensure that each entry is valid, and there are no duplicated values for the primary key."""
    primary_keys = set()
    for entry in entries:
        valid, status = validate_entry(entry)
        if not valid:
            # It might be more convenient to print out all invalid entries first.
            return False, f"Invalid entry: {entry}: {status}"
        for entry_primary_keys in entry[PRIMARY_KEY]:
            if entry_primary_key in entry_primary_keys:
                return False, f"Duplicate primary key: {entry_primary_key}"
            primary_keys.add(entry_primary_keys)
    return True


def entries_from_tsv(path):
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
                        entry[key].append(row[column_key])
        except:
            print(f"Error processing row: {row}")
            raise
        entries.append(entry)
    return entries


# TODO tsv_from_entries
def tsv_from_entries(entries, path):
    raise Exception("not implemented")


def entries_by_primary_key(entries):
    """Requires validated entries list (no duplicates)"""
    entries_by_primary_key = {}
    for entry in entries:
        for entry_primary_key in entry[PRIMARY_KEY]:
            entries_by_primary_key[entry_primary_key] = entry
    return entries_by_primary_key


if __name__ == "__main__":
    entries = entries_from_tsv("translations.tsv")
    if not validate_entries(entries):
        print("Invalid!")
    else:
        print(entries_by_primary_key(entries))
        out_path = "translations_testout.tsv"
        print(f"Dumping to {out_path}")
        tsv_from_entries(entries, out_path)
